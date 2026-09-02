---
id: p08
title_ko: Text-to-SQL 모델 (DARVIS)
title_en: Text2SQL Model (DARVIS)
org: Dfinite
period: 2024-07 ~ 2025-01
role: "SQL 생성 모델·서빙 최적화 주도 (DARVIS 제품 전체는 팀 공동)"
tags: [Enterprise-AI, LLM, Text2SQL]
angles: [engineering-craft, performance-optimization, research-depth]

card:
  ko: "온디바이스·보안 제약에서 DARVIS의 Text-to-SQL 모델을 파인튜닝·서빙 최적화"
  en: "Fine-tuned DARVIS Text2SQL under on-device, no-cloud constraints"

problem:
  goal_ko: "여러 시스템(MES·ERP·SAP·자체 DB)에 흩어진 데이터를 자연어로 질의·요약 — 스타트업 첫 제품 DARVIS의 핵심 SQL 생성 모델 구축."
  goal_en: "Build the core SQL-generation model of the startup's first product, DARVIS — querying/summarizing data scattered across MES, ERP, SAP, and in-house DBs in natural language."
  hurdle_ko: |
    - 온디바이스·보안(데이터 반출 제약) — 클라우드 대형 모델 사용 불가
    - 응답 속도(성능) 요건
    - 신입으로서 sLLM 선정·서빙 최적화·경량화를 선행연구 기반으로 주도
  hurdle_en: |
    - On-device + data-egress security rule out large cloud models
    - Response-speed (performance) requirement
    - As a junior, had to drive sLLM selection / serving optimization / lightweighting from prior work

role_groups:
  - label_ko: "SQL 생성 파인튜닝 모델을 구축하고 학습·평가 데이터를 직접 구축"
    label_en: "Built the SQL-generation fine-tuned model and its training/eval data"
    uses: [f1]
  - label_ko: "최신 프롬프팅·파인튜닝 기법을 실험·비교해 접근을 확정"
    label_en: "Experimented with and compared recent prompting/fine-tuning techniques to settle the approach"
    uses: [f2]
  - label_ko: "온디바이스 제약에 맞춰 sLLM·서빙 엔진을 선정·경량화·최적화"
    label_en: "Selected, lightweighted, and optimized the sLLM and serving engine for on-device limits"
    uses: [f4, f5]
  - label_ko: "자동차부품 제조사 첫 PoC에서 다중 시스템을 통합·배포"
    label_en: "Integrated and deployed multiple systems in the first manufacturer PoC"
    uses: [f6]

facts:
  f1: {kind: artifact, value_ko: "DARVIS Text-to-SQL에서 중간 결과를 SQL문으로 생성하는 모델의 파인튜닝을 담당하고, 평가·학습 데이터를 직접 구축", value_en: "owned fine-tuning of the model that generates SQL from intermediate results in DARVIS's Text2SQL, and built the evaluation/training data", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "스키마 injection·few-shot·chain-of-thought 프롬프팅·파인튜닝 등 최신 기법을 실험·비교", value_en: "experimented with and compared a range of recent techniques — schema injection, few-shot, chain-of-thought prompting, and fine-tuning", disclosure: public, confidence: measured}
  f3: {kind: metric, value_ko: "DARVIS Text-to-SQL은 여러 데이터베이스를 동시에 조회해 3초 이내로 결과를 요약 (제품 공개 정보)", value_en: "DARVIS Text2SQL queries multiple databases simultaneously and summarizes results within 3 seconds (public product info)", disclosure: public, confidence: measured}
  f4: {kind: decision, value_ko: "온디바이스·성능 제약 아래 품질·성능 트레이드오프를 따져 최적 sLLM과 가장 빠른 서빙 엔진을 선정하고 서빙 최적화", value_en: "under on-device and performance constraints, selected the best sLLM and fastest serving engine by weighing the quality/performance trade-off, and optimized serving", disclosure: public, confidence: measured}
  f5: {kind: decision, value_ko: "LoRA 등 경량화 파인튜닝·양자화 기법을 선행연구 기반으로 연구·적용", value_en: "researched and applied lightweight fine-tuning (e.g., LoRA) and quantization based on prior work", disclosure: public, confidence: measured}
  f6: {kind: scope, value_ko: "자동차부품 제조사 첫 PoC에서 MES·ERP·SAP·자체 DB에 산재한 데이터를 통합·연동하고, 약 6개월간 핵심 기능을 개발·배포", value_en: "with an auto-parts manufacturer as the first PoC, integrated data scattered across MES, ERP, SAP, and in-house DBs, developing and deploying core features over ~6 months", disclosure: public, confidence: measured}
  f7: {kind: adoption, value_ko: "DARVIS를 코리아크레딧뷰로(KCB) PoC에도 적용 — 수만 개 신용분석 지표의 자연어 질의, 프로파일 RAG 검색, 차트/보고서 자동화, 권한 관리 (약 1.5개월, 7개 검증 항목 완료; 정량 지표 분석 중)", value_en: "DARVIS was also applied in a Korea Credit Bureau (KCB) PoC — natural-language querying over tens of thousands of credit-analysis metrics, profile RAG search, chart/report automation, and access control (~1.5 months, 7 validation items completed; quantitative metrics under analysis)", disclosure: public, confidence: measured}

variants:
  - angle: engineering-craft
    uses: [f1, f4]
    ko: "중간 결과를 SQL로 생성하는 파인튜닝 모델을 개발하고, 온디바이스 제약에 맞춰 최적 sLLM·서빙 엔진을 선정·최적화"
    en: "Built the fine-tuned model that generates SQL from intermediate results, and selected and optimized the best sLLM and serving engine under on-device constraints"
  - angle: performance-optimization
    uses: [f3, f4]
    ko: "sLLM 경량화·양자화와 서빙 엔진 최적화로 여러 데이터베이스를 동시 조회해 3초 이내로 결과를 요약하는 성능을 확보"
    en: "Through sLLM lightweighting/quantization and serving-engine optimization, achieved querying multiple databases simultaneously with result summaries within 3 seconds"
  - angle: research-depth
    uses: [f2, f5]
    ko: "스키마 injection·few-shot·chain-of-thought·파인튜닝 등 최신 기법을 실험·비교하고, LoRA 경량화·양자화 선행연구를 재현·적용"
    en: "Experimented with and compared recent techniques (schema injection, few-shot, chain-of-thought, fine-tuning) and reproduced/applied prior work on LoRA lightweighting and quantization"

short:
  ko: >
    초기 5인 AI팀 일원으로 스타트업 첫 제품 DARVIS의 Text-to-SQL 핵심 모델을 담당. 스키마
    injection·few-shot·chain-of-thought·파인튜닝 등 최신 기법을 실험하고, 온디바이스 제약 아래 최적
    sLLM·서빙 엔진 선정과 LoRA 경량화·양자화로 성능을 확보. 자동차부품 제조사 첫 PoC에서
    MES·ERP·SAP·자체 DB를 통합해 약 6개월간 개발·배포. 제품은 여러 DB를 동시 조회해 3초 이내로
    요약(공개 정보).
  en: >
    As part of the founding 5-person AI team, owned the Text2SQL model of the startup's first
    product, DARVIS. Experimented with recent techniques (schema injection, few-shot, chain-of-thought,
    fine-tuning) and secured performance under on-device constraints via the best sLLM/serving engine
    and LoRA lightweighting/quantization. With an auto-parts manufacturer as the first PoC, integrated
    MES, ERP, SAP, and in-house DBs and shipped core features over ~6 months; the product queries
    multiple databases at once and summarizes within 3 seconds (public info).
---

## 1. 문제 정의와 제약조건
- 파편화된 MES·ERP·SAP·자체 DB 데이터를 자연어로 질의·요약
- 제약: 온디바이스·성능(응답 속도)·보안 (데이터 반출 제약)

## 2. 접근과 대안 비교
- 스키마 injection·few-shot·chain-of-thought 프롬프팅·파인튜닝 등 최신 기법을 실험·비교
- 품질/성능 트레이드오프를 따져 최적 sLLM·가장 빠른 서빙 엔진을 선정

## 3. 구현
- 중간 결과를 SQL로 생성하는 파인튜닝 모델 (평가·학습 데이터 직접 구축)
- LoRA 등 경량화 파인튜닝과 양자화, 서빙 엔진 최적화

## 4. 결과 · 배포
- 자동차부품 제조사 첫 PoC: MES·ERP·SAP·자체 DB를 통합·연동하고, 약 6개월간 핵심 기능을 개발·배포
- 제품 공개 정보: 여러 데이터베이스를 동시 조회해 3초 이내로 결과를 요약
- DARVIS를 **코리아크레딧뷰로(KCB) PoC**에도 적용 — 수만 개 신용분석 지표의 자연어 질의, 프로파일
  RAG 검색, 차트/보고서 자동화, 권한 관리 (약 1.5개월, 7개 검증 항목 완료; 정량 지표 분석 중)

## 5. 한계와 배운 점
- 온디바이스 제약에 맞춘 sLLM 선정·서빙 최적화·경량화 파인튜닝·양자화를 선행연구를 따라 진행 —
  신입으로서 난도가 높았으나 그 과정에서 빠르게 성장
