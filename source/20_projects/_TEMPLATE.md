---
# 새 프로젝트는 이 파일을 복사해 pNN_<slug>.md 로 만든다.
# 포트폴리오 카드 표준: 문제 정의(2분할) → 나의 역할(그룹) → 주요 성과.
# problem 과 role_groups 는 필수 (누락 시 validate.py 가 빌드를 막음).
id: pNN
title_ko: 프로젝트 한글 제목
title_en: Project English Title
org: Genoray            # 회사/조직
period: 2026-01 ~ 2026-06
role: "리드 (…)"        # 리드 / 주도 / 단독 / 참여 → 카드 상단 태그로 자동 도출
tags: [Medical-AI]     # vocab.yaml 의 tag 만
angles: [ownership-e2e, engineering-craft]   # vocab.yaml 의 angle, 최대 3개

# ── 문제 정의 (2분할) ─────────────────────────────────────────
problem:
  goal_ko: "무엇을 왜 풀려 했는지 — 예: 외부 솔루션 내재화, 경쟁 우위 기능 탑재."
  goal_en: "What problem this set out to solve and why."
  hurdle_ko: |
    - 알려진 제약/어려움 1
    - 알려진 제약/어려움 2
  hurdle_en: |
    - Known constraint / difficulty 1
    - Known constraint / difficulty 2

# ── 나의 역할 (그룹 = 짧은 액션 문장 라벨 + 근거 fact) ──────────
# 라벨은 그 한 줄만 읽어도 무엇을 했는지 알 수 있게. uses 로 fact 연결.
# metric·adoption fact 는 자동으로 '주요 성과'로 분리됨 → 여기엔 artifact·scope·decision 위주.
role_groups:
  - label_ko: "핵심적으로 한 일을 한 문장으로"
    label_en: "One clear action sentence"
    uses: [f1, f2]
  - label_ko: "두 번째로 한 일"
    label_en: "Second thing done"
    uses: [f3]

# ── Fact Ledger (원자 사실; 사람만 작성) ──────────────────────
# kind: metric | scope | artifact | decision | adoption
# 주요 성과 = metric(정량 지표) + adoption(도입·상태).  나의 역할 = artifact·scope·decision.
facts:
  f1: {kind: artifact, value_ko: "…", value_en: "…", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "…", value_en: "…", disclosure: public, confidence: measured}
  f3: {kind: scope,    value_ko: "…", value_en: "…", disclosure: public, confidence: measured}
  f4: {kind: metric,   value_ko: "…", value_en: "…", disclosure: public, confidence: measured}
  f5: {kind: adoption, value_ko: "…", value_en: "…", disclosure: public, confidence: measured}

# ── Narrative Variants (angle별 한 문장; 이력서·요약용) ─────────
variants:
  - angle: ownership-e2e
    uses: [f1, f4]
    ko: "…"
    en: "…"

short:
  ko: >
    2~4문장 요약.
  en: >
    2-4 sentence summary.
---

## 1. 문제 정의와 제약조건
- (problem 블록과 일관되게 서술)

## 2. 접근과 대안 비교
-

## 3. 구현
-

## 4. 검증
-

## 5. 결과
-

## 6. 한계와 다음 단계
-
