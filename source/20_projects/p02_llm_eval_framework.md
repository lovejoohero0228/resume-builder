---
id: p02
title_ko: "LLM · STT 평가 데이터셋 설계"
title_en: "LLM · STT Evaluation Dataset Design"
org: "Genoray"
period: "2026-04 ~ 2026-07"
role: "리드"
role_note_ko: "팀원 1명과 협업"
role_note_en: "With one teammate"
tags: ["Medical AI", "LLM", "STT", "Evaluation"]
angles: [modeling-foundation, engineering-craft]

problem:
  goal_ko: "음성 제어 시스템의 의도 파악 품질을 객관적으로 정량화하고, 취약 지점을 짚어 모델·프롬프트·룰 개선 근거 확보"
  goal_en: "Objectively quantify the intent-understanding quality of the voice-control system and pinpoint weak spots to justify model/prompt/rule improvements."
  hurdle_ko: |
    - 단일 정답/오답 스코어로는 명령의 어떤 요소에서 취약한지 드러나지 않음
    - 평가셋 구축·검수·중복 제거 비용이 큼
    - 임상 호출 빈도·축별 민감도 달라 균일 샘플링이 부적절
  hurdle_en: |
    - A single pass/fail score does not reveal which element of a command is weak
    - Building, reviewing, and de-duplicating the eval set is costly
    - Clinical call frequency and per-axis sensitivity differ, so uniform sampling is inappropriate

role_groups:
  - label_ko: "평가를 5개 축으로 분해해 축별 채점 프레임워크를 설계"
    label_en: "Decomposed evaluation into 5 axes and designed a per-axis scoring framework"
    uses: [f1, f2, f3]
  - label_ko: "평가 데이터셋을 생성·전수 검수·가중 샘플링을 통해 unique 400건 구축"
    label_en: "Built 400 unique items via generation, full review, and weighted sampling"
    uses: [f4, f5]
  - label_ko: "목적별 평가셋을 확장 구축 — 영어 모드·간단 명령어 모드·음성 입력 모드"
    label_en: "Extended purpose-specific eval sets — English mode, simple-command mode, voice-input mode"
    uses: [f6, f7]
  - label_ko: "동일 데이터셋·채점 기준으로 STT·LLM 모델을 비교 벤치마크"
    label_en: "Benchmarked STT and LLM models on the same dataset and scoring"
    uses: [f8, f9, f10]

facts:
  f1: {kind: artifact, value_ko: "전체 평가셋을 400건으로 구성", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "평가를 5개 축으로 분해하여 자연어 명령의 어떤 요소에서 모델이 취햑한지 pinpoint 할 수 있도록 설계 — 커맨드 명확성, 파라미터 완전성 , 컨텍스트 의존성 , STT 인식 품질, 지원범위 포함 여부", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "Tool calling task를 전제로 하여 명령의 의도를 잘 파악했는지에 더해, 커맨드 스키마를 잘 따랐는지, 도메인 정책을 잘 따랐는지 평가", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "합성 생성과 규칙 기반 생성 후 전수 검수·수정으로 gold standard 평가셋을 구축 (의도했던 축을 유지 여부 검증, 환각·어감 이탈 확인, 중복 제거)", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "임상 호출 빈도와 축별 중요도가 달라, 균일 분포 대신 (커맨드 × 평가축) 생성 개수 matrix로 빈도·중요도를 가중해 샘플링", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "목적별 데이터셋을 합산하여 최종 약 600건 활용", value_en: "", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "직접 녹음 및  TTS 활용을 통해 STT 평가셋을 생성", value_en: "", disclosure: public, confidence: measured}
  f8: {kind: artifact, value_ko: "STT 모델을 latency·CER 기준으로 클라우드·로컬 모델 비교 (Whisper, Cohere, NeMo, Gemma, Qwen 등)", value_en: "", disclosure: public, confidence: measured}
  f9: {kind: artifact, value_ko: "LLM 모델을 클라우드·로컬 모델 비교 (OpenAI, Anthropic, Gemma, Qwen 등)", value_en: "", disclosure: public, confidence: measured}
  f10: {kind: artifact, value_ko: "모델 비교의 통제 변수로 동일 입력셋·동일 채점 기준을 고정하고, 프롬프트 통일 실험과 모델별 프롬프트 다양화 실험을 병행", value_en: "Fixed identical inputs and scoring as control variables for model comparison, running both unified-prompt and per-model prompt experiments", disclosure: public, confidence: measured}
  f11: {kind: adoption, value_ko: "Speech-to-Command 프로젝트에 대한 end-to-end 평가 데이터셋 600건 이상 생성", value_en: "Generated 600+ end-to-end evaluation items for the Speech-to-Command project", disclosure: public, confidence: measured}

variants:
  - angle: modeling-foundation
    uses: [f2, f4, f5, f1]
    ko: "음성 제어 시스템 평가를 5개 축(커맨드 명확성·파라미터 완전성·컨텍스트 의존성·STT 인식·지원범위)으로 분해해 축별 채점 프레임워크를 설계하고, 합성·규칙 생성 + 전수 검수 + 가중 샘플링으로 unique 400건을 구축"
    en: "Decomposed voice-control evaluation into 5 axes (command clarity, parameter completeness, context dependency, STT quality, in-scope coverage) with a per-axis scoring framework, and built 400 unique items via synthetic/rule generation, full review, and weighted sampling"
  - angle: engineering-craft
    uses: [f8, f10, f11]
    ko: "동일 데이터셋·채점 기준을 통제변수로 STT·LLM 모델을 클라우드·로컬 비교 벤치마크(Whisper·Qwen 등), Speech-to-Command용 end-to-end 평가셋 600건 이상 생성"
    en: "Benchmarked STT and LLM models across cloud and local (Whisper, Qwen, etc.) with identical dataset and scoring as control variables, generating 600+ end-to-end evaluation items for Speech-to-Command"

short:
  ko: "음성 제어 시스템 평가를 5개 축(커맨드 명확성·파라미터 완전성·컨텍스트 의존성·STT 인식·지원범위)으로 분해해 축별 채점 프레임워크를 설계하고, 합성·규칙 생성 + 전수 검수 + 가중 샘플링으로 unique 400건을 구축"
  en: "Decomposed voice-control evaluation into 5 axes (command clarity, parameter completeness, context dependency, STT quality, in-scope coverage) with a per-axis scoring framework, and built 400 unique items via synthetic/rule generation, full review, and weighted sampling"
---
