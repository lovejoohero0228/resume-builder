"""로컬 GUI 서버 (표준 라이브러리, 무의존).

    python app/server.py         # http://127.0.0.1:8765

기능:
- 소스(.md)·프로필(.yaml) 읽기/저장
- 공고별 조립(assemble): emphasis·포함 항목·언어·detail 선택 → resume/portfolio 문자열
- 조립 결과를 브라우저에서 미리보기·편집·export (HTML/DOC/PDF는 프런트에서)
"""
from __future__ import annotations
import os
import sys
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "build"))
sys.path.insert(0, HERE)
import build as B          # noqa: E402
import yaml                # noqa: E402

ALLOWED_DIRS = (os.path.join(ROOT, "source"), os.path.join(ROOT, "profiles"))


def _safe_path(rel: str):
    """source/ · profiles/ 안의 .md/.yaml 로만 제한. 벗어나면 None."""
    if not rel or ".." in rel.replace("\\", "/").split("/"):
        return None
    p = os.path.normpath(os.path.join(ROOT, rel))
    if not any(p == d or p.startswith(d + os.sep) for d in ALLOWED_DIRS):
        return None
    if os.path.splitext(p)[1].lower() not in (".md", ".yaml", ".yml"):
        return None
    return p


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False)
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_file(self, data, ctype, filename):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _serve_asset(self, path):
        """assets/ 안의 정적 파일(이미지 등) 서빙. 경로 이탈 차단."""
        import mimetypes
        from urllib.parse import unquote
        rel = unquote(path).lstrip("/")
        if ".." in rel.replace("\\", "/").split("/"):
            return self._send(404, {"error": "not found"})
        fp = os.path.normpath(os.path.join(ROOT, rel))
        assets_dir = os.path.join(ROOT, "assets")
        if not (fp == assets_dir or fp.startswith(assets_dir + os.sep)) or not os.path.isfile(fp):
            return self._send(404, {"error": "not found"})
        ctype = mimetypes.guess_type(fp)[0] or "application/octet-stream"
        with open(fp, "rb") as f:
            data = f.read()
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _read_json(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def log_message(self, *a):
        pass  # quiet

    # ---- GET ----
    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        try:
            if u.path in ("/", "/index.html"):
                with open(os.path.join(HERE, "index.html"), encoding="utf-8") as f:
                    return self._send(200, f.read(), "text/html; charset=utf-8")
            if u.path.startswith("/assets/"):
                return self._serve_asset(u.path)
            if u.path == "/api/catalog":
                return self._send(200, B.catalog())
            if u.path == "/api/file":
                p = _safe_path(q.get("path", [""])[0])
                if not p or not os.path.exists(p):
                    return self._send(404, {"error": "not found"})
                with open(p, encoding="utf-8") as f:
                    return self._send(200, {"content": f.read()})
            if u.path == "/api/profile":
                name = q.get("name", [""])[0]
                p = _safe_path("profiles/" + name + ".yaml")
                if not p or not os.path.exists(p):
                    return self._send(404, {"error": "not found"})
                with open(p, encoding="utf-8") as f:
                    return self._send(200, {"profile": yaml.safe_load(f)})
            return self._send(404, {"error": "unknown"})
        except Exception as e:
            return self._send(500, {"error": str(e)})

    # ---- POST ----
    def do_POST(self):
        u = urlparse(self.path)
        try:
            if u.path == "/api/file":
                d = self._read_json()
                p = _safe_path(d.get("path", ""))
                if not p:
                    return self._send(400, {"error": "bad path"})
                os.makedirs(os.path.dirname(p), exist_ok=True)
                with open(p, "w", encoding="utf-8") as f:
                    f.write(d.get("content", ""))
                return self._send(200, {"ok": True})
            if u.path == "/api/assemble":
                profile = self._read_json()
                return self._send(200, B.assemble(profile))
            if u.path == "/api/resume_docx":
                d = self._read_json()
                profile = d.get("profile", {})
                lang = d.get("lang") or profile.get("lang") or "ko"
                if lang == "both":
                    lang = "en"
                a = B.assemble(profile)
                rs = a["resume_struct"].get(lang) or a["resume_struct"][a["langs"][0]]
                import docx_export
                data = docx_export.resume_docx_bytes(rs)
                return self._send_file(
                    data,
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    f"resume_{lang}.docx")
            if u.path == "/api/portfolio_pptx":
                d = self._read_json()
                profile = d.get("profile", {})
                lang = d.get("lang") or profile.get("lang") or "ko"
                if lang == "both":
                    lang = "ko"
                a = B.assemble(profile)
                lg = lang if lang in a["langs"] else a["langs"][0]
                parts = a["portfolio_parts"].get(lg, [])
                identity = a["identity"].get(lg) or {}
                target = a["resume_struct"].get(lg, {}).get("target", "")
                import pptx_export
                data, _warnings = pptx_export.portfolio_pptx_bytes(identity, target, parts, lg, ROOT)
                return self._send_file(
                    data,
                    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    f"portfolio_{lg}.pptx")
            if u.path == "/api/profile":
                d = self._read_json()
                name = d.get("name", "")
                if not re.fullmatch(r"[A-Za-z0-9._-]+", name or ""):
                    return self._send(400, {"error": "bad name"})
                p = _safe_path("profiles/" + name + ".yaml")
                if not p:
                    return self._send(400, {"error": "bad path"})
                with open(p, "w", encoding="utf-8") as f:
                    yaml.safe_dump(d.get("profile", {}), f, allow_unicode=True, sort_keys=False)
                return self._send(200, {"ok": True})
            return self._send(404, {"error": "unknown"})
        except Exception as e:
            return self._send(500, {"error": str(e)})


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"career-master GUI → http://127.0.0.1:{port}  (Ctrl+C 로 종료)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n종료")


if __name__ == "__main__":
    main()
