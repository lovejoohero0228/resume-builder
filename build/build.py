"""조립 + 검증 — 룰베이스.

    python build/build.py <profile-name>

프로필의 include 순서대로 소스를 읽어 이력서·포트폴리오를 조립한다.
{{ pXX }} 는 emphasis 우선순위에 맞는 variant 로 치환된다.
검증(validate)을 먼저 돌리고, 에러가 있으면 빌드를 중단한다.
"""
from __future__ import annotations
import os
import re
import sys
import glob

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

import validate as V

ROOT = V.ROOT
SOURCE = V.SOURCE
PROFILES = os.path.join(ROOT, "profiles")
DIST = os.path.join(ROOT, "dist")

LANG_BLOCK_RE = re.compile(r"<!--\s*lang:(\w+)\s*-->(.*?)<!--\s*/lang\s*-->", re.DOTALL)
PLACEHOLDER_RE = re.compile(r"\{\{\s*(p\d+)\s*\}\}")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


# ---------- 소스 로딩 ----------

def resolve_source_path(sid: str) -> str | None:
    """'00_identity', '10_experience/e01', '20_projects/p02' 등을 실제 파일 경로로."""
    direct = os.path.join(SOURCE, sid + ".md")
    if os.path.exists(direct):
        return direct
    matches = glob.glob(os.path.join(SOURCE, sid + "_*.md"))
    if matches:
        return matches[0]
    # 하위 디렉터리 prefix 매칭 (10_experience/e01 -> e01_*.md)
    d, base = os.path.split(sid)
    if d:
        matches = glob.glob(os.path.join(SOURCE, d, base + "_*.md"))
        if matches:
            return matches[0]
    return None


def load_projects() -> dict:
    projects = {}
    for path in glob.glob(os.path.join(SOURCE, "20_projects", "p*.md")):
        meta, body = V.parse_frontmatter(path)
        if meta and meta.get("id"):
            projects[meta["id"]] = {"meta": meta, "body": body, "path": path}
    return projects


# ---------- 나의 역할 / 주요 성과 구성 ----------

# 나의 역할(한 일들)에 들어가는 fact 종류 · 주요 성과(임팩트·지표)에 들어가는 종류
ROLE_KINDS = ("artifact", "scope", "decision")
IMPACT_KINDS = ("metric", "adoption")
KIND_GROUP_LABEL = {
    "artifact": ("구현 · 산출물", "Deliverables"),
    "decision": ("설계 · 의사결정", "Decisions"),
    "scope": ("데이터 · 범위", "Scope & scale"),
}


def parse_fact_groups(path: str) -> list:
    """frontmatter 의 facts 블록에서 '# --- 라벨 ---' 주석 기반 그룹을 추출.

    반환: [[label|None, [fid, ...]], ...]  (원문 순서). 주석이 없으면 [[None, [모든 fid]]].
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = V.FRONTMATTER_RE.match(text)
    if not m:
        return []
    groups, cur, in_facts = [], None, False
    for ln in m.group(1).split("\n"):
        top = re.match(r"^(\w[\w-]*)\s*:", ln)
        if top and ln[:1] not in (" ", "\t"):
            in_facts = top.group(1) == "facts"
            cur = None
            continue
        if not in_facts:
            continue
        gc = re.match(r"^\s*#\s*-{2,}\s*(.*?)\s*-{2,}\s*$", ln)
        if gc:
            cur = [gc.group(1).strip(), []]
            groups.append(cur)
            continue
        fk = re.match(r"^\s+(f\d+)\s*:", ln)
        if fk:
            if cur is None:
                cur = [None, []]
                groups.append(cur)
            cur[1].append(fk.group(1))
    return groups


def build_impact(mfacts: dict, lg: str) -> list:
    """주요 성과 = 결과 지표(metric) 먼저, 도입·상태(adoption) 뒤."""
    mets, ados = [], []
    for f in mfacts.values():
        if f.get("disclosure") == "internal":
            continue
        v = (f.get(f"value_{lg}") or "").strip()
        if not v:
            continue
        if f.get("kind") == "metric":
            mets.append({"kind": "metric", "value": v})
        elif f.get("kind") == "adoption":
            ados.append({"kind": "adoption", "value": v})
    return mets + ados


def _clean_group_label(label: str) -> str:
    """포트폴리오 노출용으로 그룹 라벨에서 내부 메모(예: '(구 p04)')를 제거."""
    if not label:
        return label
    return re.sub(r"\s*\(\s*구\s*p\d+\s*\)", "", label).strip()


def _apply_bullet_order(items: list, order: list) -> list:
    """items(각 dict에 'key') 를 order(키 리스트) 순으로 재배치. 모르는 key 는 원래 순서로 뒤에."""
    if not order:
        return items
    bykey, oset = {}, set(order)
    for it in items:
        bykey.setdefault(it.get("key"), it)
    seq = [bykey[k] for k in order if k in bykey]
    seq += [it for it in items if it.get("key") not in oset]
    return seq


def build_problem(meta: dict, lg: str) -> dict | None:
    """문제 정의 = 풀고자 한 문제(goal) + 제약·난점(hurdle) 2분할. 없으면 None."""
    pr = meta.get("problem") or {}
    goal = (pr.get(f"goal_{lg}") or "").strip()
    hurdle = (pr.get(f"hurdle_{lg}") or "").strip()
    if goal or hurdle:
        return {"goal": goal, "hurdle": hurdle}
    return None


def build_role_groups(meta: dict, path: str, mfacts: dict, lg: str) -> list:
    """나의 역할 = 한 일들(artifact·scope·decision)을 위계로 묶어 하위 불렛화.

    우선순위: frontmatter의 명시적 role_groups → 주석 그룹(# --- 라벨 ---) → fact 종류.
    반환: [{"label": 라벨|None, "items": [문장, ...]}, ...]  (metric·adoption 은 주요 성과로 분리)
    """
    def fval(fid):
        f = mfacts.get(fid, {}) or {}
        if f.get("disclosure") == "internal" or f.get("kind") not in ROLE_KINDS:
            return None
        return (f.get(f"value_{lg}") or "").strip() or None

    explicit = meta.get("role_groups")
    if explicit:                                       # 명시적 그룹 (액션 문장 라벨)
        out = []
        for g in explicit:
            label = (g.get(f"label_{lg}") or g.get("label_ko") or "").strip()
            items = [x for x in (fval(fid) for fid in (g.get("uses", []) or [])) if x]
            if items:
                out.append({"label": label, "items": items})
        return out

    cgroups = parse_fact_groups(path)
    if any(g[0] for g in cgroups):                     # 주석 라벨 기반
        out = []
        for label, fids in cgroups:
            items = [x for x in (fval(fid) for fid in fids) if x]
            if items:
                out.append({"label": _clean_group_label(label), "items": items})
        return out
    # 주석이 없으면 fact 종류로 묶는다
    out = []
    for kind in ROLE_KINDS:
        items = [(f.get(f"value_{lg}") or "").strip() for f in mfacts.values()
                 if f.get("kind") == kind and f.get("disclosure") != "internal"
                 and (f.get(f"value_{lg}") or "").strip()]
        if items:
            out.append({"label": KIND_GROUP_LABEL[kind][0 if lg != "en" else 1], "items": items})
    return out


# ---------- lang 필터 ----------

def strip_lang(text: str, lang: str) -> str:
    def repl(m):
        return m.group(2) if m.group(1) == lang else ""
    return LANG_BLOCK_RE.sub(repl, text)


def clean(text: str) -> str:
    text = HTML_COMMENT_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------- variant 선택 ----------

def pick_variant(pmeta: dict, emphasis: list, report: list):
    facts = pmeta.get("facts", {}) or {}
    variants = pmeta.get("variants", []) or []

    def is_public(v):
        return all(facts.get(fid, {}).get("disclosure") != "internal" for fid in v.get("uses", []))

    public_variants = [v for v in variants if is_public(v)]
    for ang in emphasis:
        for v in public_variants:
            if v.get("angle") == ang:
                return v
    if public_variants:
        chosen = public_variants[0]
        report.append(
            f"⚠ {pmeta.get('id')}: emphasis {emphasis} 에 맞는 variant 없음 "
            f"→ '{chosen.get('angle')}' 사용. assist.py 로 생성 가능"
        )
        return chosen
    return None


def pick_variant_angle(pmeta: dict, angle: str):
    """지정 angle 의 첫 public variant (없으면 None)."""
    facts = pmeta.get("facts", {}) or {}
    for v in pmeta.get("variants", []) or []:
        if v.get("angle") == angle and all(
                facts.get(f, {}).get("disclosure") != "internal" for f in v.get("uses", [])):
            return v
    return None


# ---------- 렌더링 ----------

def render_plain(path: str, lang: str) -> str:
    meta, body = V.parse_frontmatter(path)
    return clean(strip_lang(body, lang))


def render_experience(path: str, lang: str, projects: dict, emphasis: list,
                      project_order: list, max_bullets: int, report: list,
                      project_angles: dict = None) -> str:
    meta, body = V.parse_frontmatter(path)
    body = strip_lang(body, lang)

    company = meta.get(f"company_{lang}", meta.get("company_ko", ""))
    title = meta.get(f"title_{lang}", meta.get("title_ko", ""))
    period = meta.get(f"period_{lang}", meta.get("period", ""))
    if lang == "en":
        period = period.replace("현재", "Present")
    loc = meta.get(f"location_{lang}", meta.get("location_ko", ""))
    header = f"### {company} — {title}\n*{period} · {loc}*\n"

    project_angles = project_angles or {}
    ph_ids = PLACEHOLDER_RE.findall(body)
    # project_order 가 있으면 그 목록만 포함(순서는 본문 순서 유지), 없으면 전부
    kept = set(project_order) if project_order else set(ph_ids)
    budget = [max_bullets if max_bullets else 10 ** 6]

    def repl(m):
        pid = m.group(1)
        if pid not in kept:
            return ""
        proj = projects.get(pid)
        if not proj:
            report.append(f"⚠ {os.path.basename(path)}: 프로젝트 {pid} 소스 없음")
            return ""
        angs = project_angles.get(pid)
        if angs:                                   # 선택된 관점별로 한 bullet
            vs = [pick_variant_angle(proj["meta"], a) for a in angs]
        else:                                      # 폴백: emphasis 로 1개
            vs = [pick_variant(proj["meta"], emphasis, report)]
        lines = []
        for v in vs:
            if v and budget[0] > 0:
                lines.append("- " + (v.get(lang, "") or "").strip())
                budget[0] -= 1
        return "\n".join(lines)

    substituted = PLACEHOLDER_RE.sub(repl, body)
    substituted = re.sub(r"(?m)^-\s*$", "", substituted)  # 빈 bullet 제거
    return header + "\n" + clean(substituted)


def render_project(pid: str, projects: dict, lang: str, detail_level: str,
                   emphasis: list, report: list) -> str:
    proj = projects.get(pid)
    if not proj:
        report.append(f"⚠ 포트폴리오: 프로젝트 {pid} 소스 없음")
        return ""
    meta, body = proj["meta"], proj["body"]
    title = meta.get(f"title_{lang}", meta.get("title_ko", pid))
    out = [f"## {title}"]
    role = meta.get("role", "")
    period = meta.get("period", "")
    if role or period:
        out.append(f"*{role} · {period}*".strip(" ·"))

    if detail_level == "short":
        short = meta.get("short", {}) or {}
        out.append(clean(strip_lang(short.get(lang, ""), lang)))
    else:
        out.append(clean(strip_lang(body, lang)))
    return "\n\n".join(x for x in out if x).strip()


# ---------- 조립 (문자열 반환, 파일 미기록) ----------

def render_resume(profile: dict, projects: dict, lg: str, report: list) -> str:
    rconf = profile.get("resume", {}) or {}
    max_bullets = rconf.get("max_bullets_per_job", 0)
    porder = rconf.get("project_order", []) or []
    emphasis = profile.get("emphasis", []) or []
    chunks = [f"# Resume — {profile.get('target','')}\n"]
    for sid in rconf.get("include", []) or []:
        path = resolve_source_path(sid)
        if not path:
            report.append(f"⚠ resume: 소스 '{sid}' 없음")
            continue
        if "/10_experience/" in path.replace("\\", "/"):
            chunks.append(render_experience(path, lg, projects, emphasis, porder, max_bullets, report,
                                            rconf.get("project_angles", {})))
        else:
            chunks.append(render_plain(path, lg))
    return "\n\n".join(chunks)


def portfolio_parts(profile: dict, projects: dict, lg: str, report: list) -> list:
    """포트폴리오를 include 항목별 파트 리스트로 반환 (프로젝트=1파트 → 페이지 분리 export용)."""
    pconf = profile.get("portfolio", {}) or {}
    detail = pconf.get("detail_level", "full")
    emphasis = profile.get("emphasis", []) or []
    parts = []
    for sid in pconf.get("include", []) or []:
        if sid.startswith("30_methodology"):
            continue                              # 방법론 섹션은 사용하지 않음 (완전 제거)
        if sid.startswith("20_projects/"):
            pid = sid.split("/", 1)[1]
            md = render_project(pid, projects, lg, detail, emphasis, report)
            proj = projects.get(pid)
            m = proj["meta"] if proj else {}
            title = m.get(f"title_{lg}", m.get("title_ko", pid))
            if detail == "short":
                body_md = clean(strip_lang((m.get("short") or {}).get(lg, ""), lg))
            else:
                body_md = clean(strip_lang(proj["body"], lg)) if proj else ""
            # 역할: 한글은 원문, 영어는 간단 매핑 (role_en 없으므로 한글 노출 방지)
            role_raw = m.get("role", "")
            if lg == "en":
                role_disp = m.get("role_en") or (
                    "Lead" if ("리드" in role_raw or "주도" in role_raw)
                    else "Sole" if "단독" in role_raw
                    else "Contributor" if "참여" in role_raw else "")
            else:
                role_disp = role_raw
            # 카드용 구조화 데이터 (한/영 공통 · 스캔 가능)
            sel = (pconf.get("project_angles") or {}).get(pid) or (m.get("angles", []) or [])
            mfacts = m.get("facts", {}) or {}
            vmap = {}
            for v in (m.get("variants", []) or []):
                a = v.get("angle")
                if a in sel and a not in vmap and all(
                        (mfacts.get(f, {}) or {}).get("disclosure") != "internal" for f in v.get("uses", [])):
                    vmap[a] = (v.get(lg) or "").strip()
            points = [{"angle": a, "text": vmap[a]} for a in sel if a in vmap]
            pubfacts = [{"kind": f.get("kind"), "value": (f.get(f"value_{lg}") or "").strip(),
                         "confidence": f.get("confidence")}
                        for f in mfacts.values()
                        if f.get("disclosure") != "internal" and (f.get(f"value_{lg}") or "").strip()]
            role_groups = build_role_groups(m, proj["path"], mfacts, lg) if proj else []
            for _n, _g in enumerate(role_groups):
                _g["key"] = f"grp:{_n}"
            impact = build_impact(mfacts, lg)
            for _n, _it in enumerate(impact):
                _it["key"] = f"imp:{_n}"
            _bord = (pconf.get("bullet_order") or {}).get(pid) or []
            if _bord:
                role_groups = _apply_bullet_order(role_groups, [k for k in _bord if k.startswith("grp:")])
                impact = _apply_bullet_order(impact, [k for k in _bord if k.startswith("imp:")])
            _bhid = set(((pconf.get("bullet_hidden") or {}).get(pid)) or [])
            for _g in role_groups:
                _g["hidden"] = _g["key"] in _bhid
            for _it in impact:
                _it["hidden"] = _it["key"] in _bhid
            parts.append({"sid": sid, "kind": "project", "title": title, "md": md,
                          "id": pid, "org": m.get("org", ""), "period": m.get("period", ""),
                          "role": role_disp, "tags": m.get("tags", []) or [],
                          "angles": (pconf.get("project_angles") or {}).get(pid) or (m.get("angles", []) or []),
                          "points": points, "facts": pubfacts, "body_md": body_md,
                          "role_groups": role_groups,
                          "impact": impact,
                          "problem": build_problem(m, lg),
                          "card": ((m.get("card") or {}).get(lg) or "").strip(),
                          "short": clean(strip_lang((m.get("short") or {}).get(lg, ""), lg))})
        else:
            path = resolve_source_path(sid)
            if not path:
                report.append(f"⚠ portfolio: 소스 '{sid}' 없음")
                continue
            parts.append({"sid": sid, "kind": "section", "title": sid, "md": render_plain(path, lg)})
    return parts


def render_portfolio(profile: dict, projects: dict, lg: str, report: list) -> str:
    head = f"# Portfolio — {profile.get('target','')}\n"
    parts = portfolio_parts(profile, projects, lg, report)
    return "\n\n".join([head] + [p["md"] for p in parts])


# ---------- 구조화 이력서 (docx 형식 export용) ----------

def _src_text(sid: str, lg: str) -> str:
    p = resolve_source_path(sid)
    if not p:
        return ""
    _, body = V.parse_frontmatter(p)
    return clean(strip_lang(body, lg))


def _identity_struct(lg: str) -> dict:
    t = _src_text("00_identity", lg)
    lines = [l.rstrip() for l in t.split("\n")]
    idx = next((i for i, l in enumerate(lines) if re.match(r"^##\s", l)), len(lines))
    pre = [l for l in lines[:idx] if l.strip()]
    bolds = [l for l in pre if l.startswith("**")]
    name = re.sub(r"\*\*", "", bolds[0]) if bolds else re.sub(r"^#\s*", "", pre[0] if pre else "")
    rest = [l for l in pre if not l.startswith("**") and not l.startswith("#")]
    summary = " ".join(l for l in lines[idx + 1:] if l.strip())
    return {"name": name.strip(), "tagline": (rest[0].strip() if rest else ""),
            "contact": (rest[1].strip() if len(rest) > 1 else ""), "summary": summary.strip()}


def _skills_struct(lg: str, order=None, hidden=None) -> list:
    rows = []
    for l in _src_text("01_skills", lg).split("\n"):
        m = re.match(r"^-\s+(.*)$", l.strip())
        if not m:
            continue
        mm = re.match(r"^\*\*(.+?)\*\*\s*[—–-]?\s*(.*)$", m.group(1))
        if mm:
            rows.append({"label": mm.group(1).strip(), "rest": mm.group(2).strip()})
        else:
            rows.append({"label": "", "rest": m.group(1).strip()})
    for n, r in enumerate(rows):
        r["key"] = f"sk:{n}"
    if order:
        rows = _apply_bullet_order(rows, order)
    hset = set(hidden or [])
    for r in rows:
        r["hidden"] = r["key"] in hset
    return rows


def _education_struct(lg: str) -> list:
    groups, cur = [], None
    for l in _src_text("02_education", lg).split("\n"):
        h = re.match(r"^##\s+(.*)$", l.strip())
        if h:
            cur = {"title": h.group(1).strip(), "items": []}
            groups.append(cur)
            continue
        m = re.match(r"^(\s*)-\s+(.*)$", l)
        if m and cur is not None:
            cur["items"].append({"sub": len(m.group(1)) > 0, "text": m.group(2).strip()})
    return groups


def _experience_struct(path, lg, projects, emphasis, porder, max_bullets, report,
                       project_angles=None, sid="", bullet_order=None, bullet_hidden=None) -> dict:
    meta, body = V.parse_frontmatter(path)
    body = strip_lang(body, lg)
    period = meta.get(f"period_{lg}", meta.get("period", ""))
    if lg == "en":
        period = period.replace("현재", "Present")
    sections = re.split(r"(?m)^##\s+.*$", body)   # [before, context, highlights]
    ctx = re.sub(r"\s+", " ", clean(sections[1])).strip() if len(sections) > 1 else ""
    hl = sections[2] if len(sections) > 2 else ""

    project_angles = project_angles or {}
    ph_ids = PLACEHOLDER_RE.findall(hl)
    kept = set(porder) if porder else set(ph_ids)
    budget = [max_bullets if max_bullets else 10 ** 6]

    # 각 불렛에 안정적 key 부여: 프로젝트 = "p:<pid>:<angle>", 직접 작성 = "x:<n>"
    items, plain_n, lines, i = [], 0, hl.split("\n"), 0
    while i < len(lines):
        s = lines[i].strip()
        m = re.match(r"^\{\{\s*(p\d+)\s*\}\}$", s)
        if m:
            pid = m.group(1)
            proj = projects.get(pid)
            if pid in kept and proj:
                angs = project_angles.get(pid)
                pairs = ([(a, pick_variant_angle(proj["meta"], a)) for a in angs] if angs
                         else [("", pick_variant(proj["meta"], emphasis, report))])
                for ang, v in pairs:
                    if v and budget[0] > 0:
                        items.append({"key": f"p:{pid}:{ang}", "text": (v.get(lg, "") or "").strip()})
                        budget[0] -= 1
            i += 1
            continue
        if s.startswith("- "):
            buf = s[2:]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("- ") \
                    and not lines[i].strip().startswith("{{"):
                buf += " " + lines[i].strip()
                i += 1
            items.append({"key": f"x:{plain_n}", "text": re.sub(r"\s+", " ", buf).strip()})
            plain_n += 1
            continue
        i += 1

    items = [it for it in items if it["text"]]

    # 프로필에 저장된 불렛 순서 적용 (알 수 없는 key 는 원래(소스) 순서로 뒤에)
    order = (bullet_order or {}).get(sid) or []
    if order:
        oset, seq = set(order), []
        for k in order:
            for it in items:
                if it["key"] == k and it not in seq:
                    seq.append(it)
        seq += [it for it in items if it["key"] not in oset]
        items = seq

    # 숨김(제외) 처리: bullet_items 는 전부 유지(hidden 표시), 실제 렌더용 bullets 는 제외
    hset = set((bullet_hidden or {}).get(sid) or [])
    for it in items:
        it["hidden"] = it["key"] in hset

    return {"company": meta.get(f"company_{lg}", meta.get("company_ko", "")),
            "title": meta.get(f"title_{lg}", meta.get("title_ko", "")),
            "period": period, "location": meta.get(f"location_{lg}", meta.get("location_ko", "")),
            "context": ctx, "sid": sid,
            "bullets": [it["text"] for it in items if not it["hidden"]],
            "bullet_items": items}


def resume_struct(profile: dict, projects: dict, lg: str) -> dict:
    rconf = profile.get("resume", {}) or {}
    emphasis = profile.get("emphasis", []) or []
    porder = rconf.get("project_order", []) or []
    maxb = rconf.get("max_bullets_per_job", 0)
    out = {"target": profile.get("target", ""), "lang": lg,
           "identity": None, "skills": [], "experiences": [], "education": [],
           "order": []}
    scratch = []
    for sid in rconf.get("include", []) or []:
        if sid == "00_identity":
            out["identity"] = _identity_struct(lg)
            out["order"].append("identity")
        elif sid == "01_skills":
            out["skills"] = _skills_struct(lg, profile.get("skills_order"), profile.get("skills_hidden"))
            out["order"].append("skills")
        elif sid == "02_education":
            out["education"] = _education_struct(lg)
            out["order"].append("education")
        elif sid.startswith("10_experience/"):
            p = resolve_source_path(sid)
            if p:
                out["experiences"].append(
                    _experience_struct(p, lg, projects, emphasis, porder, maxb, scratch,
                                       rconf.get("project_angles", {}), sid,
                                       rconf.get("bullet_order", {}), rconf.get("bullet_hidden", {})))
                out["order"].append("experience")
    return out


def assemble(profile: dict) -> dict:
    """프로필 dict(저장 안 된 UI 입력도 가능)를 받아 조립 결과를 문자열로 반환."""
    errors, vwarnings = V.validate_all()
    lang = profile.get("lang", "ko")
    langs = ["ko", "en"] if lang == "both" else [lang]
    projects = load_projects()
    report = []
    res = {"resume": {}, "portfolio": {}, "portfolio_parts": {}, "resume_struct": {},
           "identity": {}, "skills": {}}
    for lg in langs:
        res["identity"][lg] = _identity_struct(lg)
        res["skills"][lg] = _skills_struct(lg, profile.get("skills_order"), profile.get("skills_hidden"))
        res["resume"][lg] = render_resume(profile, projects, lg, report)
        res["resume_struct"][lg] = resume_struct(profile, projects, lg)
        res["portfolio_parts"][lg] = portfolio_parts(profile, projects, lg, report)
        head = f"# Portfolio — {profile.get('target','')}\n"
        res["portfolio"][lg] = "\n\n".join([head] + [p["md"] for p in res["portfolio_parts"][lg]])
    res["warnings"] = report
    res["errors"] = errors
    res["validation_warnings"] = vwarnings
    res["langs"] = langs
    return res


def catalog() -> dict:
    """UI 카탈로그: angle 목록 · 포함 가능한 소스 · 프로젝트(변형 angle 포함) · 프로필 목록."""
    with open(os.path.join(ROOT, "vocab.yaml"), encoding="utf-8") as f:
        vocab = V.yaml.safe_load(f)
    angles = [{"id": k, "claim": (v or {}).get("claim", "")} for k, v in vocab["angles"].items()]

    projects = load_projects()
    plist = []
    for pid, proj in sorted(projects.items()):
        m = proj["meta"]
        vangles = sorted({(v or {}).get("angle") for v in (m.get("variants") or []) if v.get("angle")})
        plist.append({
            "id": pid,
            "sid": "20_projects/" + pid,          # id 기반 (조립 로직·기존 프로필과 일치)
            "title_ko": m.get("title_ko", pid), "title_en": m.get("title_en", pid),
            "angles": m.get("angles", []) or [], "variant_angles": vangles,
            "tags": m.get("tags", []) or [], "org": m.get("org", ""),
        })

    experiences = []
    for path in sorted(glob.glob(os.path.join(SOURCE, "10_experience", "e*.md"))):
        m, _ = V.parse_frontmatter(path)
        base = os.path.splitext(os.path.basename(path))[0]
        eid = (m or {}).get("id") or base
        experiences.append({
            "sid": "10_experience/" + eid,        # id 기반 (기존 프로필과 일치)
            "company_ko": (m or {}).get("company_ko", base),
            "company_en": (m or {}).get("company_en", base),
            "projects": (m or {}).get("projects", []) or [],
        })

    plain = []
    for sid in ["00_identity", "01_skills", "02_education", "90_appendix"]:
        if resolve_source_path(sid):
            plain.append(sid)

    profiles = [os.path.splitext(os.path.basename(p))[0]
                for p in sorted(glob.glob(os.path.join(PROFILES, "*.yaml")))
                if not os.path.basename(p).startswith("_")]

    # 편집 가능한 실제 파일 목록 (소스 편집 탭용)
    files = []
    for p in sorted(glob.glob(os.path.join(SOURCE, "**", "*.md"), recursive=True)):
        files.append(os.path.relpath(p, ROOT).replace("\\", "/"))
    for p in sorted(glob.glob(os.path.join(PROFILES, "*.yaml"))):
        files.append(os.path.relpath(p, ROOT).replace("\\", "/"))

    return {"angles": angles, "projects": plist, "experiences": experiences,
            "plain": plain, "profiles": profiles,
            "tags": vocab.get("tags", {}), "files": files}


# ---------- 리포트 ----------

def collect_report_facts(projects: dict) -> list:
    lines = []
    for pid, proj in sorted(projects.items()):
        for fid, fact in (proj["meta"].get("facts", {}) or {}).items():
            if fact.get("confidence") in ("estimated", "recalled"):
                lines.append(f"- {pid}:{fid} [{fact['confidence']}] {fact.get('value_ko','')}")
    return lines


def collect_markers() -> list:
    lines = []
    for path in glob.glob(os.path.join(SOURCE, "**", "*.md"), recursive=True):
        with open(path, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if V.MARKER_RE.search(line):
                    rel = os.path.relpath(path, ROOT)
                    lines.append(f"- {rel}:{n}  {line.strip()}")
    return lines


# ---------- 메인 ----------

def build(profile_name: str):
    ppath = os.path.join(PROFILES, profile_name + ".yaml")
    if not os.path.exists(ppath):
        print(f"✗ 프로필 없음: {ppath}")
        sys.exit(1)
    with open(ppath, encoding="utf-8") as f:
        profile = V.yaml.safe_load(f)

    # 1) 검증 먼저 — 에러 시 중단
    errors, warnings = V.validate_all()
    for w in warnings:
        print(f"⚠ {w}")
    if errors:
        for e in errors:
            print(f"✗ {e}")
        print(f"\n빌드 중단: 검증 에러 {len(errors)}건")
        sys.exit(1)

    lang = profile.get("lang", "ko")
    langs = ["ko", "en"] if lang == "both" else [lang]
    projects = load_projects()

    outdir = os.path.join(DIST, profile_name)
    os.makedirs(outdir, exist_ok=True)
    report = []

    for lg in langs:
        write(os.path.join(outdir, f"resume_{lg}.md"), render_resume(profile, projects, lg, report))
        write(os.path.join(outdir, f"portfolio_{lg}.md"), render_portfolio(profile, projects, lg, report))

    # 리포트
    rep = ["# 빌드 리포트", f"프로필: {profile_name}", ""]
    rep += ["## 재확인 필요 fact (confidence: estimated | recalled)"]
    rep += collect_report_facts(projects) or ["- (없음)"]
    rep += ["", "## 미확인 마커 (TODO / [확인필요])"]
    rep += collect_markers() or ["- (없음)"]
    rep += ["", "## 빌드 경고"]
    rep += (report or ["- (없음)"])
    write(os.path.join(outdir, "_report.md"), "\n".join(rep))

    print(f"\n✅ 빌드 완료 → {os.path.relpath(outdir, ROOT)}")
    for lg in langs:
        print(f"   resume_{lg}.md, portfolio_{lg}.md")
    print("   _report.md")


def write(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python build/build.py <profile-name>")
        sys.exit(1)
    build(sys.argv[1])
