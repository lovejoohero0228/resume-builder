"""이력서를 Resume 1 서식(Arial · 남색 #153D63 · 섹션 대문자+하단선 · 회사 볼드)의
진짜 .docx 로 생성. Word 네이티브 서식이라 Word→PDF 가 미리보기와 일관됨.

resume_struct(dict) -> docx bytes
"""
from __future__ import annotations
import io
import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x15, 0x3D, 0x63)
GRAY = RGBColor(0x55, 0x55, 0x55)
BLACK = RGBColor(0x11, 0x11, 0x11)
ARIAL = "Arial"
EA = "Malgun Gothic"   # 한글 fallback


def _run(p, text, color=BLACK, bold=False, size=9.0):
    r = p.add_run(text)
    f = r.font
    f.name = ARIAL
    f.size = Pt(size)
    f.color.rgb = color
    r.bold = bold
    rpr = r._element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    rf.set(qn("w:ascii"), ARIAL)
    rf.set(qn("w:hAnsi"), ARIAL)
    rf.set(qn("w:cs"), ARIAL)
    rf.set(qn("w:eastAsia"), EA)
    return r


def _rich(p, text, color=BLACK, bold=False, size=9.0):
    """`**bold**` 토글을 반영해 여러 run 으로 추가."""
    for i, seg in enumerate(str(text).split("**")):
        if seg:
            _run(p, seg, color, bold or (i % 2 == 1), size)


def _bottom_border(p, color="DBE0E8", sz="6"):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), sz)
    b.set(qn("w:space"), "2")
    b.set(qn("w:color"), color)
    pbdr.append(b)
    pPr.append(pbdr)


def _para(doc, before=0.0, after=1.0):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.06
    return p


def _section(doc, title):
    p = _para(doc, before=9, after=2)
    _run(p, str(title).upper(), NAVY, True, 10)
    _bottom_border(p)


def resume_docx_bytes(rs: dict) -> bytes:
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = ARIAL
    normal.font.size = Pt(9)
    rpr = normal.element.get_or_add_rPr()
    rf = rpr.get_or_add_rFonts()
    rf.set(qn("w:eastAsia"), EA)

    sec = doc.sections[0]
    sec.top_margin = Inches(0.5)
    sec.bottom_margin = Inches(0.5)
    sec.left_margin = Inches(0.6)
    sec.right_margin = Inches(0.6)

    lang = rs.get("lang", "en")
    labels = ({"p": "프로필", "s": "기술 스택", "e": "경력"} if lang == "ko"
              else {"p": "Profile", "s": "Technical Skills", "e": "Experience"})

    def block_identity():
        idn = rs.get("identity") or {}
        if not idn:
            return
        p = _para(doc, after=1)
        _run(p, idn.get("name", ""), BLACK, True, 17)
        if idn.get("tagline"):
            p = _para(doc, after=1)
            _rich(p, idn["tagline"], NAVY, True, 9)
        if idn.get("contact"):
            p = _para(doc, after=4)
            _run(p, idn["contact"], GRAY, False, 8.5)
        if idn.get("summary"):
            _section(doc, labels["p"])
            _rich(_para(doc, after=2), idn["summary"], BLACK, False, 9)

    def block_skills():
        vis = [s for s in (rs.get("skills") or []) if not s.get("hidden")]
        if not vis:
            return
        _section(doc, labels["s"])
        for s in vis:
            p = _para(doc, after=1)
            if s.get("label"):
                _run(p, s["label"] + "   ", NAVY, True, 9)
            _rich(p, s.get("rest", ""), BLACK, False, 9)

    def block_education():
        for g in rs.get("education", []) or []:
            _section(doc, g.get("title", ""))
            for it in g.get("items", []):
                p = _para(doc, after=1)
                if it.get("sub"):
                    p.paragraph_format.left_indent = Inches(0.18)
                _rich(p, it.get("text", ""), GRAY if it.get("sub") else BLACK, False, 9)

    exps = list(rs.get("experiences") or [])
    _exp_state = {"i": 0, "header": False}

    def block_experience():
        # order 리스트에는 경력이 1개당 'experience' 토큰 1개 → 순서대로 하나씩 렌더
        if _exp_state["i"] >= len(exps):
            return
        if not _exp_state["header"]:
            _section(doc, labels["e"])
            _exp_state["header"] = True
        e = exps[_exp_state["i"]]
        _exp_state["i"] += 1
        p = _para(doc, before=4, after=0)
        _run(p, e.get("company", ""), BLACK, True, 9)
        meta = " · ".join(x for x in [e.get("title"), e.get("period"), e.get("location")] if x)
        if meta:
            _run(p, "   —   " + meta, GRAY, False, 9)
        if e.get("context"):
            _rich(_para(doc, after=1), e["context"], GRAY, False, 9)
        for b in e.get("bullets", []):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.06
            _rich(p, b, BLACK, False, 9)

    blocks = {"identity": block_identity, "skills": block_skills,
              "experience": block_experience, "education": block_education}
    order = rs.get("order") or ["identity", "skills", "experience", "education"]
    # 'experience' 토큰이 order에 없으면(구버전) 남은 경력을 한 번에
    if "experience" not in order and exps:
        order = order + ["experience"] * len(exps)
    for tok in order:
        fn = blocks.get(tok)
        if fn:
            fn()

    bio = io.BytesIO()
    doc.save(bio)
    return bio.getvalue()
