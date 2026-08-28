---
id: p02
title_ko: LLM · STT 평가 설계 (5축 프레임워크 + 모델 비교)
title_en: LLM / STT Evaluation Design (5-Axis Framework + Model Comparison)
org: Genoray
period: 2026-04 ~ 2026-07
role: "리드 (팀원 1명과 협업)"
tags: [Medical-AI, LLM, Speech, NLP]
angles: [modeling-foundation, ownership-e2e, engineering-craft]

card:
  ko: "단일 점수로는 안 보이던 음성 이해의 취약점을 5축 평가 프레임워크로 정량 진단"
  en: "Diagnosed voice-understanding weak spots via a 5-axis evaluation framework"

problem:
  goal_ko: "음성 제어 시스템의 의도 파악 품질을 객관적으로 정량화하고, 취약 지점을 짚어 모델·프롬프트·룰 개선 근거 확보"
  goal_en: "Objectively quantify the voice-control system's intent-understanding quality and pinpoint weak spots to guide model/prompt/rule improvements."
  hurdle_ko: |
    - 단일 정답/오답 스코어로는 명령의 어떤 요소에서 취약한지 드러나지 않음
    - gold standard 평가셋 구축·검수·중복 제거 비용이 큼
    - 임상 호출 빈도·축별 민감도가 달라 균일 샘플링이 부적절
  hurdle_en: |
    - A single pass/fail score can't reveal which elements of a command are weak
    - Building/verifying a gold-standard set (dedup, consistency) is costly
    - Uniform sampling is wrong — clinical call frequency and per-axis sensitivity differ

role_groups:
  - label_ko: "평가를 5개 축으로 분해해 축별 채점 프레임워크를 설계"
    label_en: "Decomposed evaluation into 5 axes and designed the per-axis scoring framework"
    uses: [f2, f3, f13, f14, f1]
  - label_ko: "gold standard 평가셋을 생성·전수 검수·가중 샘플링으로 구축"
    label_en: "Built a gold-standard evaluation set via generation, full review, and weighted sampling"
    uses: [f4, f5]
  - label_ko: "목적별 평가셋을 확장 구축 (영어 모드·간단 명령어·STT)"
    label_en: "Built purpose-specific evaluation sets (English mode, simple-command, STT)"
    uses: [f6, f7, f8, f9]
  - label_ko: "동일 입력셋·채점 기준으로 STT·LLM 모델을 비교"
    label_en: "Compared STT and LLM models under a shared input set and scoring criteria"
    uses: [f10, f11, f12]

facts:
  # --- 5축 평가 프레임워크 ---
  f1: {kind: scope, value_ko: "전체 평가셋을 400건으로 구성", value_en: "a 400-item evaluation set", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "평가를 5개 축으로 분해 — CMD_KW / COMPLETE / INPUT_Q / SCOPE / CTX_DEP", value_en: "decomposed evaluation into 5 axes — CMD_KW / COMPLETE / INPUT_Q / SCOPE / CTX_DEP", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "축별 채점 기준을 정의한 평가 프레임워크", value_en: "an evaluation framework defining per-axis scoring criteria", disclosure: public, confidence: measured}
  # --- 평가 데이터 구축 ---
  f4: {kind: decision, value_ko: "합성 생성과 규칙 기반 생성 후 전수 검수·수정으로 gold standard 평가셋을 구축 (동일 커맨드·동일 축을 유지하는지 검증, 환각·어감 이탈 확인, 중복 제거)", value_en: "Built a gold-standard evaluation set via synthetic + rule-based generation followed by full manual review and correction (verifying each item stays in the same command and axis, checking for hallucination or nuance drift, removing duplicates)", disclosure: public, confidence: measured}
  f5: {kind: decision, value_ko: "임상 호출 빈도와 축별 민감도/특이도가 달라, 균일 분포 대신 (커맨드 × 평가축) 생성 개수 matrix로 빈도·중요도를 가중해 샘플링", value_en: "Since clinical call frequency and per-axis sensitivity/specificity differ, sampled by a (command × axis) generation-count matrix weighted by frequency and importance instead of uniformly", disclosure: public, confidence: measured}
  f6: {kind: scope, value_ko: "영어 발화 모드용 데이터셋을 약 100건 추가 구축", value_en: "Built an additional ~100-item dataset for an English-speech mode", disclosure: public, confidence: estimated}
  f7: {kind: scope, value_ko: "자연어 대신 간단 명령어 방식 데이터를 약 100건 추가 구축", value_en: "Built ~100 additional items in a simple-command (non-natural-language) style", disclosure: public, confidence: estimated}
  f8: {kind: scope, value_ko: "목적별 데이터셋을 합산 약 600건 활용", value_en: "Used ~600 items in total across purpose-specific datasets", disclosure: public, confidence: estimated}
  f9: {kind: artifact, value_ko: "400건 평가셋을 녹음한 뒤 TTS로 약 2배 확장해 STT 평가셋을 생성", value_en: "Recorded the 400-item set and expanded it ~2x via TTS to produce the STT evaluation set", disclosure: public, confidence: measured}
  # --- 모델 비교 ---
  f10: {kind: scope, value_ko: "STT 모델을 latency·CER 기준으로 클라우드·로컬에서 비교 (Whisper, Cohere, NeMo, Gemma, Qwen 등)", value_en: "Compared STT models on latency and CER across cloud and local options (Whisper, Cohere, NeMo, Gemma, Qwen)", disclosure: public, confidence: measured}
  f11: {kind: scope, value_ko: "LLM 모델을 클라우드·로컬로 비교 (OpenAI, Anthropic, Gemma, Qwen 등)", value_en: "Compared LLM models across cloud and local options (OpenAI, Anthropic, Gemma, Qwen)", disclosure: public, confidence: measured}
  f12: {kind: decision, value_ko: "모델 비교의 통제 변수로 동일 입력셋·동일 채점 기준을 고정하고, 프롬프트 통일 실험과 모델별 프롬프트 다양화 실험을 병행", value_en: "Controlled model comparison with a shared input set and shared scoring criteria, running both a unified-prompt experiment and per-model prompt-variation experiments", disclosure: public, confidence: measured}
  # --- 설계 판단 ---
  f13: {kind: decision, value_ko: "단일 정답/오답 스코어가 놓치는 지점 — 자연어 명령의 어떤 요소에서 모델·프롬프트·룰이 취약/강한지 축별로 pinpoint하기 위해 평가를 5개 축으로 분해", value_en: "Decomposed evaluation into 5 axes to pinpoint — beyond a single pass/fail score — which elements of a natural-language command each model, prompt, or rule handles well or poorly", disclosure: public, confidence: measured}
  f14: {kind: decision, value_ko: "모든 모델을 tool calling 전제로 커맨드 스키마 출력에 맞춰, LLM 출력 품질 평가를 음성 명령 이해 평가와 동일하게 정의", value_en: "Defined every model around tool calling that emits a command schema, so evaluating LLM output quality is equivalent to evaluating voice-command understanding", disclosure: public, confidence: measured}

variants:
  - angle: modeling-foundation
    uses: [f2, f1]
    ko: "LLM 출력 품질을 CMD_KW·COMPLETE·INPUT_Q·SCOPE·CTX_DEP 5개 축으로 분해하고 400건 평가셋으로 축별 채점 기준을 설계"
    en: "Decomposed LLM output quality into 5 axes (CMD_KW, COMPLETE, INPUT_Q, SCOPE, CTX_DEP) and designed per-axis scoring on a 400-item evaluation set"
  - angle: modeling-foundation
    uses: [f13]
    ko: "단일 정답/오답 스코어를 넘어, 명령의 어떤 요소에서 시스템이 취약한지 축별로 진단하도록 평가를 5개 축으로 분해"
    en: "Went beyond pass/fail scoring by decomposing evaluation into 5 axes that diagnose which command elements the system handles poorly"
  - angle: modeling-foundation
    uses: [f4, f5]
    ko: "합성·규칙 기반 생성 후 전수 검수로 gold standard 평가셋을 구축하고, 임상 호출 빈도·축별 민감도/특이도를 반영한 (커맨드 × 평가축) matrix로 비균일 샘플링"
    en: "Built a gold-standard evaluation set via synthetic and rule-based generation with full manual review, sampled non-uniformly by a (command × axis) matrix reflecting clinical call frequency and per-axis sensitivity/specificity"
  - angle: ownership-e2e
    uses: [f3, f4]
    ko: "평가 축 분해·채점 기준 정의·gold standard 평가셋 구축까지 평가 프레임워크 전체를 설계"
    en: "Designed the full evaluation framework — axis decomposition, scoring criteria, and a gold-standard evaluation set"
  - angle: engineering-craft
    uses: [f12]
    ko: "동일 입력셋·동일 채점 기준을 통제하고 모델별 프롬프트 실험을 병행한 재현 가능한 모델 비교 프로토콜을 구축"
    en: "Built a reproducible model-comparison protocol controlled by a shared input set and scoring criteria, with per-model prompt experiments"

short:
  ko: >
    음성 제어 시스템의 의도 파악 품질을 정량화하기 위한 평가 설계. LLM 출력 품질을 5개 축
    (CMD_KW·COMPLETE·INPUT_Q·SCOPE·CTX_DEP)으로 분해, 합성·규칙 기반 생성 후 전수
    검수로 400건 gold standard 평가셋 구축(임상 호출 빈도·축별 민감도/특이도 반영한
    커맨드×축 matrix 샘플링). 영어 모드·간단 명령어 데이터 추가로 목적별 약 600건 활용,
    동일 입력셋·채점 기준으로 클라우드·로컬 STT·LLM 모델 비교.
  en: >
    Evaluation design for quantifying voice-control system quality. Decomposed LLM output quality
    into 5 axes (CMD_KW, COMPLETE, INPUT_Q, SCOPE, CTX_DEP) and built a 400-item gold-standard
    evaluation set via synthetic and rule-based generation with full manual review (sampled by a
    command × axis matrix reflecting clinical call frequency and per-axis sensitivity/specificity).
    Added English-mode and simple-command data for ~600 items across purposes, and compared
    cloud/local STT and LLM models under a shared input set and scoring criteria.
---

## 1. 문제 정의와 제약조건
- 음성 제어 시스템(p01)의 **의도 파악 품질**을 객관적으로 평가하고, 개선 지점을 특정해야 함
- 단일 스코어(정답/오답)는 동작 검증(단위 테스트)에는 충분하지만, 모델·프롬프트·룰 설계에 따라
  **자연어 명령의 어떤 요소**에서 취약/강한지를 드러내지 못함
- 전제: 모든 모델 구조가 **tool calling**을 전제로 최종 커맨드 스키마에 맞춘 출력을 내므로,
  LLM 출력 품질 평가 = 음성 명령 이해 평가와 동일

## 2. 접근과 대안 비교
축별 취약/강한 조합을 파악해 의도 파악 시스템의 특성을 이해하고 문제점을 pinpoint하려 평가를 5개 축으로 분해.

| 대안 | 장점 | 탈락 / 채택 사유 |
|---|---|---|
| 단일 스코어 (정답/오답) | 단순, 회귀 검증 용이 | 취약점 pinpoint 불가, 축별 강약 조합 파악 불가 |
| **채택: 5축 분해** | 명령의 요소별 강약을 객관적으로 진단하고 개선 지점을 특정 | 축·카테고리 설계와 라벨링 비용은 감수 |

## 3. 구현 — 5개 평가 축

- 다이어그램: assets/diagrams/p02_eval_axes.mmd

| 축 | 이름 | 질문 | 카테고리 |
|---|---|---|---|
| **CMD_KW** | 커맨드 명확성 | 이 발화가 어떤 커맨드인지 얼마나 명확한가? | direct / indirect / partial_kw |
| **COMPLETE** | 파라미터 완전성 | 필요한 파라미터가 얼마나 주어졌는가? | full / partial / none / conflicting / - |
| **INPUT_Q** | STT 입력 품질 | STT 전사 결과가 얼마나 깨끗한가? | substitution / insertion / repetition / deletion |
| **SCOPE** | 지원 범위 포함 여부 | 지원 범위 내인가? | in_domain / out_of_domain / multi_intent |
| **CTX_DEP** | 컨텍스트 의존성 | 직전 컨텍스트가 있어야 해석되는가? | context_dependent |

**축1 · CMD_KW (커맨드 명확성)**
- `direct` — 커맨드 키워드가 발화에 직접 등장
- `indirect` — 키워드 없이 상태·기능으로 추론
- `partial_kw` — 키워드가 없거나 일부만 있어 커맨드 특정 불가

**축2 · COMPLETE (파라미터 완전성)**
- `full` — 필수+선택 파라미터 모두 명시
- `partial` — 선택 파라미터만 누락 (기본값 매핑)
- `none` — 필수 파라미터 누락 → 예외 반환
- `conflicting` — 파라미터 값 충돌
- `-` — 파라미터 논의 불가 (OOD 또는 partial_kw)

**축3 · INPUT_Q (STT 입력 품질)**
- `substitution` — 단어 오인식 (음성 치환)
- `insertion` — 불필요한 텍스트 삽입
- `repetition` — 전사 텍스트 반복
- `deletion` — 전사 텍스트 누락

**축4 · SCOPE (지원 범위 포함 여부)**
- `in_domain` — 명세 커맨드로 귀결 가능
- `out_of_domain` — 명세 외 커맨드, **거부가 정답**
- `multi_intent` — 커맨드 2개 이상

**축5 · CTX_DEP (컨텍스트 의존성)**
- `context_dependent` — 직전 커맨드가 있어야 해석 가능

> 축을 나눔으로써 "정답률 X%"를 넘어, 예컨대 *indirect + partial 조합에서 특정 모델이 약하다*처럼
> 취약 조합을 지목하고 프롬프트·룰을 표적 개선할 수 있다.

## 4. 검증 (데이터셋 · 프로토콜)

### 4-1. 평가 데이터 구축
- **생성**: 합성 생성 + 규칙 기반 생성 후 **전수 검수·수정** → gold standard화
  (생성물이 동일 커맨드·동일 축에 머무는지, 환각·미묘한 어감 차이로 축을 벗어났는지 검증, 중복 제거)
  — 직접 수정 작업이 가장 까다로웠던 지점
- **커버리지**: 임상 호출 빈도와 축별 민감도/특이도가 다르므로, 균일 분포가 아니라
  **(커맨드 × 평가축) 생성 개수 matrix**로 빈도·중요도를 가중해 샘플링
- **규모**: 기본 평가셋 400건 + 영어 발화 모드 약 100건 + 간단 명령어 방식 약 100건
  → 목적별 합산 약 600건
- **STT 평가셋**: 400건을 녹음 + TTS로 약 2배 확장
- 규모가 이 수준에 그친 이유: gold standard 검증·중복 제거·라벨 정합성 확보 비용

### 4-2. 모델 비교 프로토콜
- **통제 변수**: 동일 입력셋, 동일 채점 기준
- **프롬프트**: 통일 실험과 함께, 모델 특성 차이를 반영한 **모델별 프롬프트 다양화 실험** 병행
- **비교 대상**: STT (Whisper, Cohere, NeMo, Gemma, Qwen 등 클라우드·로컬) — latency·CER,
  LLM (OpenAI, Anthropic, Gemma, Qwen 등 클라우드·로컬)

## 5. 결과
- 결과 수치·모델 선정 결론은 대외 공개 보류

## 6. 한계
- gold standard 검증·중복 제거·라벨 정합성 확보 비용이 커서 데이터 규모가 제한됨
