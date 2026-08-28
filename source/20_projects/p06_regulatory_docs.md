---
id: p06
title_ko: 규제 대응 기술 문서화 (MFDS, 음성 AI 파트)
title_en: Regulatory Technical Documentation (MFDS, Voice-AI Part)
org: Genoray
period: 2026-05 ~ 2026-08
role: 참여 (음성인식 AI 기술 파트 담당)
tags: [Medical-AI]
angles: [stakeholder-alignment]

card:
  ko: "심사자와 엔지니어링의 설명 간극을 메워 음성 AI 기술을 MFDS 재심사 문서로 작성"
  en: "Bridged the reviewer–engineering gap in the C-arm module's MFDS docs"

problem:
  goal_ko: "C-arm 음성 제어 모듈의 MFDS 재심사 통과를 목표로, 음성인식 AI 기술을 비전문 심사자도 평가할 수 있게 문서화"
  goal_en: "Get the C-arm voice-control module through MFDS re-review by documenting the voice-recognition AI so a non-engineering reviewer can evaluate it."
  hurdle_ko: |
    - 규제 심사자와 엔지니어링 사이의 설명 간극 — 음성 AI 구조를 비전문가가 평가 가능하게 전달
    - 규제 인증 절차 자체가 처음 접하는 영역 (규제 도메인 학습 병행)
  hurdle_en: |
    - An explanation gap between regulators and engineering — the voice-AI architecture must be legible to a non-expert
    - The certification process itself was new territory (learning the regulatory domain in parallel)

role_groups:
  - label_ko: "MFDS 재심사용 음성인식 AI 기술 문서를 비전문 심사자 관점으로 작성"
    label_en: "Authored the MFDS re-review voice-AI technical section for a non-engineering reviewer"
    uses: [f1]

facts:
  f1: {kind: artifact, value_ko: "MFDS 재심사 제출용 보충 기술문서 중 음성인식 AI 파트(음성 모듈 아키텍처·룰 엔진 설계)를 비전문 심사자가 평가 가능한 형태로 작성", value_en: "Authored the voice-recognition AI section of the supplementary technical documentation for the MFDS re-review submission — framing the voice module architecture and rule-engine design for a non-engineering reviewer", disclosure: public, confidence: measured}
  f2: {kind: adoption, value_ko: "C-arm 음성 제어 모듈이 규제 인증을 진행 중", value_en: "C-arm voice-control module in regulatory certification", disclosure: public, confidence: recalled}

variants:
  - angle: stakeholder-alignment
    uses: [f1]
    ko: "MFDS 재심사 제출에서 음성인식 AI 기술 파트(음성 모듈 아키텍처·룰 엔진 설계)를 비전문 심사자가 평가할 수 있는 보충 기술문서로 작성"
    en: "For the MFDS re-review submission, authored the voice-recognition AI technical section — framing the voice module architecture and rule-engine design so a non-engineering reviewer could evaluate it"

short:
  ko: >
    C-arm 음성 제어 모듈의 MFDS 재심사 제출에서 음성인식 AI 기술 파트를 담당. 음성 모듈
    아키텍처·룰 엔진 설계를 비전문 심사자가 평가 가능하게 보충 기술문서로 작성. (인증 진행 중)
  en: >
    Handled the voice-recognition AI part of the MFDS re-review submission for the C-arm
    voice-control module — writing supplementary technical documentation that frames the voice
    module architecture and rule-engine design for a non-engineering reviewer. (In certification.)
---

## 1. 문제 정의와 제약조건
- 규제 심사자와 엔지니어링 사이의 설명 간극 — 음성 AI 모듈의 구조를 비전문가가 평가 가능하게 전달
- 인증 절차 자체가 처음 접하는 영역 (규제 도메인 학습 병행)

## 2. 한 일
- MFDS 재심사 제출용 보충 기술문서 중 **음성인식 AI 기술 파트**를 담당·작성
- 음성 모듈 아키텍처·룰 엔진 설계를 비전문 심사자 관점에서 기술

## 3. 결과 · 상태
- 인증 진행 중

## 4. 한계와 다음 단계
- 진행 중 — 인증 경과에 따라 보완
