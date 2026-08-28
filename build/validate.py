"""검증기 — 룰베이스. 위반 시 빌드를 중단한다 (build.py 에서 import).

지시서 v3 §5-3 의 검사표를 구현한다.
독립 실행도 가능:  python build/validate.py
"""
from __future__ import annotations
import os
import re
import sys
import glob
import yaml

# Windows 콘솔(cp949)에서도 유니코드 기호가 깨지지 않도록 UTF-8 강제
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "source")
PROJECTS_DIR = os.path.join(SOURCE, "20_projects")

VALID_KINDS = {"metric", "scope", "artifact", "decision", "adoption"}
VALID_CONFIDENCE = {"measured", "estimated", "recalled"}
VALID_DISCLOSURE = {"public", "internal", "range_only"}

# 추적 고유명사 — variant 가 이 목록의 단어를 쓰면 참조 fact 에도 있어야 한다 (§5-3 규칙 2).
# 일반 기술 약어(STT, NLU, RAG ...)는 의도적으로 제외한다: 사실을 새로 만드는 것이 아니라
# 제품/프레임워크/기관/회사 등 "이름"의 무단 도입만 막는다.
TRACKED_ENTITIES = [
    "YOLO", "Detectron2", "Detectron", "MMDetection", "Mask2Former", "U-Net",
    "nnU-Net", "SAM", "ONNX", "TorchScript", "vLLM", "LLaMA", "Qwen", "BERT",
    "DeepDRR", "FFmpeg", "Whisper", "Faster Whisper", "Superset", "DARVIS",
    "Genoray", "Dfinite", "Blind", "MFDS", "DICOM", "Text-to-SQL",
    "HRNet", "Nuitka", "Cython", "MaskDINO", "LangChain", "BM25", "LoRA",
]

# 완화·구간 표현 (estimated/recalled fact 참조 variant 에 강제)
HEDGE_KO = ["약", "가량", "여", "이상", "미만", "내외", "초과", "~", "-"]
HEDGE_EN = ["about", "approx", "around", "over", "under", "~", "+", "roughly", "at least"]

NUM_RE = re.compile(r"\d+(?:\.\d+)?%?[KkMmBb]?")
DIGIT_RUN_RE = re.compile(r"\d+(?:\.\d+)?")
MARKER_RE = re.compile(r"TODO\b|\[확인필요\]")


# ---------- frontmatter 파싱 ----------

FRONTMATTER_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?(.*)$", re.DOTALL)


def parse_frontmatter(path: str):
    """(meta_dict, body_str) 반환. frontmatter 가 없으면 (None, 전체본문).

    구분자는 **한 줄 전체가 정확히 `---`** 인 경우만 인정한다. (프론트매터 주석 안의
    `# --- ... ---` 같은 문자열이 파싱을 끊는 것을 방지.)
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, m.group(2)


def _load_vocab():
    with open(os.path.join(ROOT, "vocab.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------- 개별 검사 ----------

def _numbers(s: str):
    return set(DIGIT_RUN_RE.findall(s or ""))


def _entities(s: str):
    s = s or ""
    found = []
    for ent in TRACKED_ENTITIES:
        # 단어 경계 기준 (특수문자 포함 이름 때문에 단순 substring + 경계 보정)
        if ent in s:
            found.append(ent)
    return set(found)


def validate_project(path: str, vocab: dict):
    """한 프로젝트 파일 검증. (errors, warnings) 리스트 반환."""
    errors, warnings = [], []
    meta, body = parse_frontmatter(path)
    name = os.path.basename(path)
    if meta is None:
        return [f"{name}: frontmatter 없음"], []

    valid_angles = set(vocab["angles"].keys())
    banned = set(vocab["banned_terms"]["ko"]) | set(vocab["banned_terms"]["en"])

    # angle 목록
    p_angles = meta.get("angles", []) or []
    for a in p_angles:
        if a not in valid_angles:
            errors.append(f"{name}: vocab 에 없는 angle '{a}'")
    if len(p_angles) > 3:
        errors.append(f"{name}: angle {len(p_angles)}개 (최대 3개)")

    # tag 목록
    valid_tags = set()
    for group in vocab["tags"].values():
        valid_tags.update(group)
    for t in meta.get("tags", []) or []:
        if t not in valid_tags:
            errors.append(f"{name}: vocab 에 없는 tag '{t}'")

    # facts enum
    facts = meta.get("facts", {}) or {}
    for fid, fact in facts.items():
        if fact.get("kind") not in VALID_KINDS:
            errors.append(f"{name}:{fid}: 잘못된 kind '{fact.get('kind')}'")
        if fact.get("confidence") not in VALID_CONFIDENCE:
            errors.append(f"{name}:{fid}: 잘못된 confidence '{fact.get('confidence')}'")
        if fact.get("disclosure") not in VALID_DISCLOSURE:
            errors.append(f"{name}:{fid}: 잘못된 disclosure '{fact.get('disclosure')}'")

    # variants
    for i, v in enumerate(meta.get("variants", []) or []):
        tag = f"{name}: variant#{i} (angle={v.get('angle')})"
        ang = v.get("angle")
        if ang not in valid_angles:
            errors.append(f"{tag}: vocab 에 없는 angle")
        uses = v.get("uses", []) or []
        ref_facts = []
        for fid in uses:
            if fid not in facts:
                errors.append(f"{tag}: uses 의 fact '{fid}' 없음")
            else:
                ref_facts.append(facts[fid])

        ko, en = v.get("ko", "") or "", v.get("en", "") or ""
        if not ko.strip():
            errors.append(f"{tag}: ko 비어 있음")
        if not en.strip():
            errors.append(f"{tag}: en 비어 있음")

        # 금지어
        for term in banned:
            if re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", ko + " " + en):
                errors.append(f"{tag}: 금지어 '{term}'")

        # 참조 fact 의 숫자/고유명사 집합
        ref_nums, ref_ents = set(), set()
        for fct in ref_facts:
            joined = f"{fct.get('value_ko','')} {fct.get('value_en','')}"
            ref_nums |= _numbers(joined)
            ref_ents |= _entities(joined)

        for n in _numbers(ko + " " + en):
            if n not in ref_nums:
                errors.append(f"{tag}: 숫자 '{n}' 가 참조 fact 에 없음")
        for e in _entities(ko + " " + en):
            if e not in ref_ents:
                errors.append(f"{tag}: 고유명사 '{e}' 가 참조 fact 에 없음")

        # performance-optimization 은 metric fact 필수
        if ang == "performance-optimization":
            if not any(f.get("kind") == "metric" for f in ref_facts):
                errors.append(f"{tag}: performance-optimization 인데 metric fact 미참조")

        # estimated/recalled fact 참조 시 완화 표현 강제
        soft = any(f.get("confidence") in ("estimated", "recalled") for f in ref_facts)
        if soft:
            if not any(h in ko for h in HEDGE_KO):
                errors.append(f"{tag}: estimated/recalled fact 참조인데 ko 에 완화·구간 표현 없음")
            if not any(h.lower() in en.lower() for h in HEDGE_EN):
                errors.append(f"{tag}: estimated/recalled fact 참조인데 en 에 완화·구간 표현 없음")

    # 포트폴리오 표준 형식 — 모든 프로젝트 통일 (문제 정의 2분할 + 나의 역할 그룹)
    problem = meta.get("problem")
    if not isinstance(problem, dict):
        errors.append(f"{name}: problem 블록 없음 (goal_ko/goal_en/hurdle_ko/hurdle_en 필요)")
    else:
        for k in ("goal_ko", "goal_en", "hurdle_ko", "hurdle_en"):
            if not (problem.get(k) or "").strip():
                errors.append(f"{name}: problem.{k} 비어 있음")

    rgroups = meta.get("role_groups") or []
    if not rgroups:
        errors.append(f"{name}: role_groups 없음 (나의 역할 그룹 — 액션 문장 라벨 + uses)")
    for i, g in enumerate(rgroups):
        g = g or {}
        if not (g.get("label_ko") or "").strip():
            errors.append(f"{name}: role_groups#{i} label_ko 비어 있음")
        if not (g.get("label_en") or "").strip():
            errors.append(f"{name}: role_groups#{i} label_en 비어 있음")
        uses = g.get("uses", []) or []
        if not uses:
            errors.append(f"{name}: role_groups#{i} uses 비어 있음")
        for fid in uses:
            if fid not in facts:
                errors.append(f"{name}: role_groups#{i} uses 의 fact '{fid}' 없음")

    # 마커 (경고)
    if MARKER_RE.search(body):
        warnings.append(f"{name}: TODO / [확인필요] 마커 잔존")

    return errors, warnings


def validate_all():
    vocab = _load_vocab()
    all_errors, all_warnings = [], []
    for path in sorted(glob.glob(os.path.join(PROJECTS_DIR, "p*.md"))):
        e, w = validate_project(path, vocab)
        all_errors += e
        all_warnings += w
    return all_errors, all_warnings


if __name__ == "__main__":
    errors, warnings = validate_all()
    for w in warnings:
        print(f"⚠ {w}")
    for e in errors:
        print(f"✗ {e}")
    if errors:
        print(f"\n검증 실패: 에러 {len(errors)}건, 경고 {len(warnings)}건")
        sys.exit(1)
    print(f"검증 통과 (경고 {len(warnings)}건)")
