"""프로필 하나를 조립해 포트폴리오 PPTX 를 파일로 저장 (GUI 없이 한 방에).

    python app/make_pptx.py <profile-name> [out.pptx]

기본 출력: dist/<profile>/portfolio_<lang>.pptx
서버(app/server.py)의 /api/portfolio_pptx 와 동일한 조립·렌더 경로를 사용한다.
"""
from __future__ import annotations
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "build"))
sys.path.insert(0, HERE)

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import yaml
import build as B
import pptx_export


def main():
    if len(sys.argv) < 2:
        print("사용법: python app/make_pptx.py <profile-name> [out.pptx]")
        sys.exit(1)
    name = sys.argv[1]
    ppath = os.path.join(ROOT, "profiles", name + ".yaml")
    if not os.path.exists(ppath):
        print(f"✗ 프로필 없음: {ppath}")
        sys.exit(1)
    with open(ppath, encoding="utf-8") as f:
        profile = yaml.safe_load(f)

    a = B.assemble(profile)
    if a.get("errors"):
        for e in a["errors"]:
            print(f"✗ {e}")
        print(f"\n빌드 중단: 검증 에러 {len(a['errors'])}건")
        sys.exit(1)

    lang = profile.get("lang", "ko")
    lg = "ko" if lang == "both" else lang
    lg = lg if lg in a["langs"] else a["langs"][0]

    parts = a["portfolio_parts"].get(lg, [])
    identity = a["identity"].get(lg) or {}
    target = a["resume_struct"].get(lg, {}).get("target", "")
    appendix = B.activity_groups(lg)
    data, warnings = pptx_export.portfolio_pptx_bytes(identity, target, parts, lg, ROOT,
                                                      appendix_groups=appendix)

    out = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(ROOT, "dist", name, f"portfolio_{lg}.pptx")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)

    for w in a.get("warnings", []) + warnings:
        print(f"⚠ {w}")
    n_proj = sum(1 for p in parts if p.get("kind") == "project")
    print(f"\n✅ PPT 생성 → {os.path.relpath(out, ROOT)}  (커버 1 + 프로젝트 {n_proj}장)")


if __name__ == "__main__":
    main()
