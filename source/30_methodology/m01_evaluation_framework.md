# 방법론 — AI 평가 설계

> p02(5축 평가 프레임워크 + 모델 비교 평가)를 재료로 한 독립 챕터.
> LLM 평가 직무 공고에서는 이것이 사실상 메인 포트폴리오다. 개별 프로젝트에 종속시키지 않는다.
> (Phase 2 에서 p02 를 끝까지 완성한 뒤 본문을 채운다.)

<!-- lang:ko -->
## 1. 평가 축을 왜 5개로 분해했는가
단일 정답/오답 스코어는 동작 검증(단위 테스트)에는 충분하지만, 모델·프롬프트·룰 설계에 따라
자연어 명령의 *어떤 요소*에서 취약/강한지를 드러내지 못한다. 취약/강한 조합을 지목해 개선
지점을 특정하기 위해 평가를 5개 축으로 분해했다.

- **CMD_KW** 커맨드 명확성 — direct / indirect / partial_kw
- **COMPLETE** 파라미터 완전성 — full / partial / none / conflicting / -
- **INPUT_Q** STT 입력 품질 — substitution / insertion / repetition / deletion
- **SCOPE** 지원 범위 — in_domain / out_of_domain / multi_intent
- **CTX_DEP** 컨텍스트 의존성 — context_dependent

전제: 모든 모델이 tool calling으로 커맨드 스키마 출력을 내므로, LLM 출력 품질 평가가 곧
음성 명령 이해 평가가 된다. (축별 카테고리 상세는 p02 참조)

## 2. 데이터셋 구성·샘플링 원칙
- 합성 생성 + 규칙 기반 생성 후 **전수 검수·수정**으로 gold standard화 (동일 커맨드·동일 축
  유지 검증, 환각·어감 이탈 확인, 중복 제거)
- 임상 호출 빈도와 축별 민감도/특이도가 다르므로 균일 분포가 아니라 **(커맨드 × 평가축)
  생성 개수 matrix**로 빈도·중요도를 가중해 샘플링
- 규모: 기본 400건 + 영어 발화 모드 약 100건 + 간단 명령어 방식 약 100건 → 목적별 약 600건

## 3. 판정·거부 처리
- 평가(SCOPE 축): `out_of_domain` 은 **거부가 정답**으로 규정
- 시스템(런타임): 범위 밖·불확실 입력은 명령 종류에 따라 거부/무시 또는 재질의를 혼용 (UX 고려) — 상세 p01

## 4. 모델 비교 실험 설계 (공정 비교를 위한 통제 변수)
- 통제 변수: 동일 입력셋, 동일 채점 기준
- 프롬프트: 통일 실험과 모델별 프롬프트 다양화 실험 병행 (모델 특성 차이 반영)
- 비교 대상·지표: STT(latency·CER), LLM — 상세는 p02 참조
<!-- /lang -->

<!-- lang:en -->
## 1. Why decompose evaluation into 5 axes
A single pass/fail score is enough to verify behavior (like a unit test), but it does not reveal
*which element* of a natural-language command a given model, prompt, or rule is weak or strong on.
To pinpoint weak/strong combinations and target improvements, evaluation was decomposed into 5 axes.

- **CMD_KW** command clarity — direct / indirect / partial_kw
- **COMPLETE** parameter completeness — full / partial / none / conflicting / -
- **INPUT_Q** STT input quality — substitution / insertion / repetition / deletion
- **SCOPE** support scope — in_domain / out_of_domain / multi_intent
- **CTX_DEP** context dependency — context_dependent

Premise: every model emits a command schema via tool calling, so evaluating LLM output quality is
equivalent to evaluating voice-command understanding. (Per-axis category details in p02.)

## 2. Dataset composition & sampling principles
- Synthetic + rule-based generation, then full manual review/correction to a gold standard (verify
  each item stays in the same command and axis; check hallucination or nuance drift; remove duplicates)
- Since clinical call frequency and per-axis sensitivity/specificity differ, sampled by a
  (command x axis) generation-count matrix weighted by frequency and importance, not uniformly
- Scale: 400 base + ~100 English-mode + ~100 simple-command → ~600 items across purposes

## 3. Rejection / out-of-scope handling
- Evaluation (SCOPE axis): `out_of_domain` is defined such that rejection is the correct answer
- System (runtime): out-of-scope/uncertain input is handled by rejecting/ignoring or re-querying,
  chosen by command type for UX — see p01

## 4. Controlled model-comparison experiment design
- Controlled variables: shared input set, shared scoring criteria
- Prompts: both a unified-prompt experiment and per-model prompt-variation experiments (models differ)
- Targets/metrics: STT (latency, CER), LLM — details in p02
<!-- /lang -->
