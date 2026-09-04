---
id: p12
title_ko: "학습 데이터 구축 · 어노테이션 툴 개발"
title_en: "Training Data Construction & Annotation Tool"
org: "Genoray"
period: "2026-02 ~ 2026-10"
role: "리드"
role_note_ko: "어노테이션 툴 개발 — 단독  /  학습 데이터 구축 — 기획팀과 협업"
role_note_en: "Annotation tool — solo / data construction — with the planning team"
tags: ["Data Construction", "SAM", "Annotation Tool"]
angles: [ownership-e2e, engineering-craft, stakeholder-alignment]

problem:
  goal_ko: "모델 개발에 필요한 파노라마 학습 데이터를 구축하는 것 — 라벨링 체계 정의, 도구 개발, 라벨러 교육, 비즈니스 결정까지"
  goal_en: "Construct the panoramic training data needed for modeling — labeling scheme, tooling, labeler training, and business decisions."
  hurdle_ko: |
    - 데이터 보안 문제로 상용 툴·외부 매입 불가
    - 제품 요구사항 불명확 — '무엇을 어떻게 라벨링할지'부터 정의 필요
    - 아무도 해보지 않은 새로운 성격의 데이터 구축 프로젝트
  hurdle_en: |
    - Data security ruled out commercial tools and external purchase
    - Unclear product requirements — even 'what to label and how' had to be defined
    - A new kind of data-construction project no one had done before

role_groups:
  - label_ko: "학습용 데이터 약 4,000장을 구축·운영"
    label_en: "Built and operated ~4,000 training images"
    uses: [f1, f2]
  - label_ko: "라벨링 체계·가이드라인·라벨러 교육까지의 프로세스 정립"
    label_en: "Established the process — labeling scheme, guidelines, and labeler training"
    uses: [f3, f4, f5]
  - label_ko: "medical SAM·보안을 갖춘 커스텀 어노테이션 툴 개발"
    label_en: "Built a custom annotation tool with medical SAM and security"
    uses: [f6, f7, f8, f9]
  - label_ko: "자체 구축과 외부 매입을 분석해 방향 결정"
    label_en: "Analyzed in-house build vs external purchase to decide direction"
    uses: [f10, f11]

facts:
  f1: {kind: artifact, value_ko: "파노라마 원본 약 2~3만 장을 획득하고, 선별 기준에 따라 데이터를 선별한 뒤 라벨링 및 QC를 통해 학습용 데이터 약 4.000장 구축", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "원본 데이터 자동 전처리 파이프라인 구축 : 비식별화 →  등급 분류 → 사전 annotation 추론 → 배포", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "요구사항이 불명확한 상태에서 기획 관점까지 반영해 라벨링 체계를 scratch부터 정립 주도", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "라벨링 operation을 위해 작업자 교육용 가이드라인 문서 제작— 라벨링 항목별 일반 지침, Edge 케이스 지침 등", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "대학병원 전문의 8명과 치기공사·위생사 5인을 교육·온보딩·관리", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "오픈소스 라벨링 툴이 목적에 맞지 않아, Windows 기반 커스텀 어노테이션 툴을 자체 개발", value_en: "Built a custom Windows-based annotation tool in-house since open-source tools did not fit the purpose", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "라벨링 툴용 SAM 모델을 자사 치아 데이터로 LoRA 파인튜닝 → 치아 마스크 라벨링 시간·비용 절감", value_en: "", disclosure: public, confidence: measured}
  f8: {kind: artifact, value_ko: "커스텀 툴 기능 — medical SAM 탑재, 브러쉬 기반 라벨 자유 편집, Human error 방지 UX/UI, 검수 편의 기능", value_en: "", disclosure: public, confidence: measured}
  f9: {kind: artifact, value_ko: "자사 데이터·자체 툴의 유출 방지 보안 시스템 구축 — 로그인 서버, 데이터 파일 암호화, 작업 로그 기반 퍼포먼스 모니터링", value_en: "", disclosure: public, confidence: measured}
  f10: {kind: artifact, value_ko: "약 1억 규모 예산 내에서 자체 구축과 외부 매입을 비교하고, 매입 후보 데이터가 부적합하다는 분석 의견을 근거 제시", value_en: "", disclosure: public, confidence: measured}
  f11: {kind: artifact, value_ko: "외부 매입 후보 데이터를 샘플링·통계 분석해, 라벨 품질 등 적합성을 모델링 관점에서 평가하고 매입 부적합 의견을 제시", value_en: "", disclosure: public, confidence: measured}
  f12: {kind: adoption, value_ko: "커스텀 라벨링 툴 개발", value_en: "Built a custom labeling tool", disclosure: public, confidence: measured}
  f13: {kind: adoption, value_ko: "학습용 고품질 데이터 약 4,000장 구축", value_en: "Built ~4,000 high-quality training images", disclosure: public, confidence: measured}
  f14: {kind: adoption, value_ko: "학습 데이터 구축 프로세스 정립", value_en: "Established the training-data construction process", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f3, f13]
    ko: "파노라마 학습 데이터 구축을 라벨링 체계 정의·도구 개발·라벨러 교육·매입 의사결정까지 end-to-end로 주도, 고품질 학습 데이터 약 4,000장을 구축"
    en: "Drove panoramic training-data construction end to end — labeling scheme, tooling, labeler training, and purchase decisions — building ~4,000 high-quality training images"
  - angle: engineering-craft
    uses: [f6, f7, f9]
    ko: "오픈소스로는 목적에 안 맞아 Windows 기반 커스텀 어노테이션 툴을 자체 개발 — medical SAM 탑재(자사 데이터로 LoRA 파인튜닝), 데이터 암호화·작업 로그 모니터링 보안 시스템 구축"
    en: "Built a custom Windows annotation tool in-house — medical SAM (LoRA-fine-tuned on our data), with data encryption and work-log monitoring for security"
  - angle: stakeholder-alignment
    uses: [f5, f10]
    ko: "라벨링 가이드라인을 정립하고 대학병원 전문의 8명·치기공사·위생사 5인을 교육·온보딩했으며, 약 1억 예산에서 자체 구축과 외부 매입을 분석해 방향을 결정"
    en: "Established labeling guidelines and trained/onboarded 8 specialists and 5 technicians/hygienists, and analyzed in-house build vs external purchase to set direction"

short:
  ko: "파노라마 학습 데이터 구축을 라벨링 체계 정의·도구 개발·라벨러 교육·매입 의사결정까지 end-to-end로 주도, 고품질 학습 데이터 약 4,000장을 구축"
  en: "Drove panoramic training-data construction end to end — labeling scheme, tooling, labeler training, and purchase decisions — building ~4,000 high-quality training images"
---
