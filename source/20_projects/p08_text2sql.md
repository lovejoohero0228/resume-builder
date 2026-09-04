---
id: p08
title_ko: "Text2SQL 모델 개발 — DARVIS AI"
title_en: "Text2SQL Model Development — DARVIS AI"
org: "Dfinite"
period: "2024-07 ~ 2024-12"
role: "참여"
role_note_ko: "SQL 생성 모델·서빙 최적화 담당 —  DARVIS AI 개발 팀 총 4인"
role_note_en: "Owned SQL-generation model & serving optimization — DARVIS AI team of 4"
tags: ["LLM", "Text2SQL"]
angles: [ownership-e2e, engineering-craft, shipping-delivery]

problem:
  goal_ko: "여러 시스템(MES·ERP·SAP·자체 DB)에 흩어진 데이터를 자연어로 질의하고 요약된 결과를 제공하는 것 — 프로덕트의 핵심 기능"
  goal_en: "Query data scattered across systems (MES, ERP, SAP, in-house DB) in natural language and return summarized results — the product's core feature."
  hurdle_ko: |
    - 온디바이스· 고객사 데이터 보안 — 클라우드 LLM 사용 불가
    - 응답 속도 요구사항 충족 요건,  sLLM 선정·서빙 최적화·경량화 진행
    - 신규 프로덕트 개발 단계에서 핵심 모듈의 책임자로서 선행 연구와 실험을 주도
  hurdle_en: |
    - On-device / client data security — cloud LLMs not allowed
    - Response-speed requirements — sLLM selection, serving optimization, and compression
    - As owner of the core module in a new product, drove the research and experiments

role_groups:
  - label_ko: "SQL 생성 파인튜닝 모델을 fine-tuning하고, 학습 및 평가 데이터를 직접 구축"
    label_en: "Fine-tuned the SQL-generation model and built the training/eval data"
    uses: [f1, f2]
  - label_ko: "“자연어 쿼리 → 쿼리 파싱 결과 → SQL문”으로 구성된 학습·평가 데이터셋 구축"
    label_en: "Built a training/eval dataset of (natural-language query → parsed query → SQL)"
    uses: [f3]
  - label_ko: "온디바이스 제약에 맞춰 sLLM·서빙 엔진을 선정, 이후 경량화·최적화 주도"
    label_en: "Selected the sLLM and serving engine under on-device constraints, then drove compression and optimization"
    uses: [f4, f5]
  - label_ko: "자동차부품 제조사 첫 PoC에서 다중 시스템을 통합·배포"
    label_en: "Integrated and deployed multiple systems in the first PoC at an auto-parts maker"
    uses: [f6]

facts:
  f1: {kind: artifact, value_ko: "파싱된 유저 입력과 테이블 스키마 정보를 바탕으로 SQL문을 생성하는 모델의 개발을 담당하고, SQL문의 검증 로직을 설계", value_en: "Owned development of the SQL-generation model from parsed user input and table schema, and designed the SQL validation logic", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "스키마 injection·few-shot·chain-of-thought prompting·fine-tuning 등 최신 기법을 실험·비교", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "SQL문의 다양한 문법 요소를 조합하여 최종 SQL문을 조립한 뒤, 자연어 쿼리까지 역순으로 생성하는 방식을 통해 데이터셋 구축", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "온디바이스·성능 제약 아래 품질·성능 트레이드오프를 따져 최적 sLLM과 가장 서빙 엔진을 선정하고 서빙 최적화", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "LoRA 등 경량화 파인튜닝·양자화 기법을 선행연구 기반으로 연구·적용", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "자동차부품 제조사 첫 PoC에서 MES·ERP·SAP·자체 DB에 산재한 데이터를 통합·연동하고, 약 6개월간 핵심 기능을 개발·배포 ·개선", value_en: "", disclosure: public, confidence: measured}
  f7: {kind: adoption, value_ko: "여러 데이터베이스를 자연어로 동시에 조회해, 3초 이내로 결과를 요약", value_en: "Queried multiple databases at once in natural language and summarized results within 3 seconds", disclosure: public, confidence: measured}
  f8: {kind: adoption, value_ko: "DARVIS의 핵심 기능의 초기 모델 개발 담당 및 성공적인 첫 PoC 진행", value_en: "Owned the initial model for DARVIS's core feature and ran a first PoC", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f2, f3, f7, f8]
    ko: "제조 데이터를 자연어로 질의하는 DARVIS의 SQL 생성 모델을 담당 — 스키마 injection·few-shot·CoT·파인튜닝을 비교하고 학습·평가 데이터셋을 직접 구축, 여러 DB를 3초 이내로 요약 응답"
    en: "Owned DARVIS's SQL-generation model for querying manufacturing data in natural language — compared schema injection, few-shot, CoT, and fine-tuning, built the train/eval dataset, and summarized across multiple DBs within 3 seconds"
  - angle: engineering-craft
    uses: [f4, f5]
    ko: "온디바이스·보안 제약(클라우드 LLM 불가)에서 최적 sLLM·서빙 엔진을 선정하고 LoRA 경량화·양자화로 서빙 최적화"
    en: "Under on-device/security constraints (no cloud LLM), selected the sLLM and serving engine and optimized serving with LoRA compression and quantization"
  - angle: shipping-delivery
    uses: [f6]
    ko: "자동차부품 제조사 첫 PoC에서 MES·ERP·SAP·자체 DB를 통합·연동해 약 6개월간 핵심 기능을 개발·배포"
    en: "In the first PoC at an auto-parts maker, integrated MES/ERP/SAP/in-house DBs and developed and deployed the core feature over about 6 months"

short:
  ko: "제조 데이터를 자연어로 질의하는 DARVIS의 SQL 생성 모델을 담당 — 스키마 injection·few-shot·CoT·파인튜닝을 비교하고 학습·평가 데이터셋을 직접 구축, 여러 DB를 3초 이내로 요약 응답"
  en: "Owned DARVIS's SQL-generation model for querying manufacturing data in natural language — compared schema injection, few-shot, CoT, and fine-tuning, built the train/eval dataset, and summarized across multiple DBs within 3 seconds"
---
