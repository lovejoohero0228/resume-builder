---
id: p12
title_ko: 학습 데이터 구축 · 어노테이션 툴
title_en: Training-Data Pipeline & Annotation Tooling
org: Genoray
period: 2026-02 ~ 2026-10
role: "AI팀 대표 단독 (기획·임상 담당자와 조율)"
tags: [Medical-AI, Vision]
angles: [ownership-e2e, engineering-craft, stakeholder-alignment]

card:
  ko: "반출 제약·불명확한 요구 속에서 파노라마 학습 데이터를 체계부터 툴까지 직접 구축"
  en: "Built panoramic training data from scratch under egress limits & unclear specs"

problem:
  goal_ko: "모델 개발에 필요한 파노라마 학습 데이터를 라벨링 체계부터 도구까지 처음부터 자체 구축."
  goal_en: "Build the panoramic training data needed for modeling entirely in-house — from the labeling scheme to the tooling."
  hurdle_ko: |
    - 원내 데이터 반출 제약 — 상용 툴·외부 매입 불가
    - 제품 요구사항 불명확 — '무엇을 어떻게 라벨링할지'부터 정의 필요
    - 아무도 해보지 않은 새 영역
  hurdle_en: |
    - Data-egress restrictions rule out commercial tools and external data purchase
    - Product requirements unclear — had to define what and how to label from scratch
    - A green-field area no one had done before

role_groups:
  - label_ko: "자체 구축과 외부 매입을 분석해 방향을 결정"
    label_en: "Analyzed build-vs-buy and decided the direction"
    uses: [f4, f5, f1]
  - label_ko: "라벨링 체계·가이드라인을 scratch부터 정립"
    label_en: "Established the labeling scheme and guidelines from scratch"
    uses: [f12, f2]
  - label_ko: "medical SAM·보안을 갖춘 커스텀 어노테이션 툴을 개발"
    label_en: "Built a custom annotation tool with medical SAM and security"
    uses: [f6, f7, f8, f14]
  - label_ko: "원본 2~3만 장에서 학습용 약 4,000장을 구축·운영"
    label_en: "Turned ~20–30k raw images into ~4,000 training images and ran the pipeline"
    uses: [f3]
  - label_ko: "전문의·치기공사 등 라벨러를 교육·관리"
    label_en: "Trained and managed labelers (specialists, technicians)"
    uses: [f9, f10]

facts:
  f1: {kind: decision, value_ko: "원내 데이터 반출 제약으로, 상용 어노테이션 툴 대신 자체 개발을 선택", value_en: "Built an in-house annotation tool instead of a commercial one, due to data-egress restrictions", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "라벨링 가이드라인 문서를 작성 — 클래스 정의, 경계 케이스 판정 규칙, 불일치 조정 절차", value_en: "Authored labeling guidelines — class definitions, edge-case adjudication rules, disagreement resolution", disclosure: public, confidence: measured}
  f3: {kind: scope, value_ko: "파노라마 원본 약 2~3만 장을 획득하고, 선별 기준·자동화 파이프라인(QC→DB→자동 재학습)으로 학습용 약 4,000장을 구축", value_en: "acquired ~20,000-30,000 raw panoramic images and built ~4,000 training images via selection criteria and an automated pipeline (QC -> database -> automated retraining)", disclosure: public, confidence: estimated}
  f4: {kind: decision, value_ko: "약 1억 규모 예산 내에서 자체 구축과 외부 매입을 비교하고, 매입 후보 데이터가 부적합하다는 의견을 근거로 자체 구축으로 결론", value_en: "Within a ~100M KRW budget, compared building in-house vs. purchasing external data and concluded to build in-house, based on a finding that the candidate purchased data was unsuitable", disclosure: public, confidence: estimated}
  f5: {kind: decision, value_ko: "외부 매입 후보 데이터를 샘플링·통계 분석해, 라벨 품질 등 적합성을 모델링 관점에서 평가하고 매입 의견을 제시", value_en: "Sampled and statistically analyzed candidate purchase data to assess label quality and fitness from a modeling standpoint, and issued the purchase recommendation", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "오픈소스 라벨링 툴이 목적에 맞지 않아, 해당 코드를 참고해 Windows 기반 커스텀 어노테이션 툴을 자체 개발", value_en: "Since open-source labeling tools were unfit for the purpose, built a custom Windows annotation tool in-house, referencing the open-source code", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "커스텀 툴 기능 — medical SAM 탑재, 라벨 자유 편집, 논의가 필요한 객체 표시, 검수 시 모아보기, 라벨 항목 누락 방지 UX", value_en: "custom tool features — embedded medical SAM, free label editing, flagging objects needing discussion, review-mode aggregation, and a UX that prevents missing any label item", disclosure: public, confidence: measured}
  f8: {kind: artifact, value_ko: "자사 데이터·라벨 유출 방지 보안, 로그인 서버, 사용자 로그 트래킹 기반 라벨링 퍼포먼스 모니터링을 구현", value_en: "implemented security against leakage of in-house data/labels, a login server for data protection, and label-performance monitoring via user-log tracking", disclosure: public, confidence: measured}
  f9: {kind: artifact, value_ko: "라벨링·검수 기준을 문서화하고, 외주 작업자를 다회 교육", value_en: "documented labeling/review standards and ran repeated training sessions for external annotators", disclosure: public, confidence: measured}
  f10: {kind: scope, value_ko: "대학병원 전문의 8명과 치기공사·위생사 5인을 교육·온보딩·관리", value_en: "Trained and onboarded 8 university-hospital specialists and 5 dental technicians / hygienists", disclosure: public, confidence: measured}
  f11: {kind: adoption, value_ko: "참고한 오픈소스 라벨링 툴에 유용한 기능을 기여(contribute)", value_en: "Contributed useful features back to the open-source labeling tool referenced", disclosure: public, confidence: measured}
  f12: {kind: decision, value_ko: "요구사항이 불명확한 상태에서 기획 관점까지 반영해 라벨링 체계를 scratch부터 정립하고, 툴·전처리까지 구축", value_en: "With product requirements still unclear, established the labeling system from scratch — accounting for the planning perspective — and built the tooling and preprocessing", disclosure: public, confidence: measured}
  f13: {kind: adoption, value_ko: "구축한 데이터·파이프라인이 후속 프로젝트의 기본 테스트·재학습 기반으로 재사용", value_en: "Reused as the default data / retraining basis on follow-on projects", disclosure: public, confidence: recalled}
  f14: {kind: artifact, value_ko: "라벨링 가속용으로 dental panorama 치아 분할 SAM 모델을 파인튜닝해 라벨링 툴에 탑재 (상세 p13)", value_en: "fine-tuned a SAM model for dental-panorama teeth segmentation and embedded it in the labeling tool to accelerate labeling (see p13)", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1, f6, f3]
    ko: "라벨링 규칙 정립, 커스텀 어노테이션 툴 개발, 학습용 약 4,000장 구축까지 학습 데이터 구축 전 과정을 AI팀 대표로 소유"
    en: "As the AI team's lead, owned the training-data pipeline end to end — labeling rules, a custom annotation tool, and building ~4,000 training images"
  - angle: ownership-e2e
    uses: [f12]
    ko: "요구사항이 불명확한 상태에서 기획 관점까지 반영해 라벨링 체계를 scratch부터 정립하고, 툴·전처리까지 구축"
    en: "With product requirements still unclear, established the labeling system from scratch — accounting for the planning perspective — and built the tooling and preprocessing"
  - angle: engineering-craft
    uses: [f6, f7]
    ko: "오픈소스 툴이 목적에 맞지 않아, 코드를 참고해 medical SAM 탑재·라벨 누락 방지 UX·검수 모아보기를 갖춘 Windows 커스텀 어노테이션 툴을 개발"
    en: "Since open-source tools were unfit, built a custom Windows annotation tool with an embedded medical SAM, a miss-proof labeling UX, and review-mode aggregation, referencing the open-source code"
  - angle: engineering-craft
    uses: [f8]
    ko: "자사 데이터·라벨 유출 방지 보안, 로그인 서버, 사용자 로그 트래킹 기반 라벨링 퍼포먼스 모니터링까지 툴에 구현"
    en: "Built into the tool: security against data/label leakage, a login server, and label-performance monitoring via user-log tracking"
  - angle: stakeholder-alignment
    uses: [f4]
    ko: "매입 후보 데이터가 부적합하다는 의견을 근거로 기획팀과 조율해, 약 1억 예산 방향을 자체 구축으로 관철"
    en: "Aligned with the planning team using the finding that candidate purchase data was unsuitable, steering the ~100M KRW budget toward building in-house"
  - angle: stakeholder-alignment
    uses: [f9]
    ko: "라벨링·검수 기준 문서화와 외주 작업자 다회 교육으로 라벨 품질을 정렬"
    en: "Documented labeling/review standards and ran repeated training for external annotators to align label quality"

short:
  ko: >
    모델링에 필요한 파노라마 학습 데이터를 처음부터 구축. 약 1억 예산 내에서 자체 구축과 외부 매입을
    비교 — 매입 후보 데이터를 샘플링·통계 분석해 부적합 의견을 내고 자체 구축으로 결론. 원본 약 2~3만
    장에서 선별·자동화 파이프라인으로 학습용 약 4,000장을 구축하고, medical SAM 탑재·보안·로그 트래킹을
    갖춘 Windows 커스텀 어노테이션 툴을 개발. 라벨링 가이드라인을 문서화하고, 전문의 8명과 치기공사/위생사
    5인을 교육·관리.
  en: >
    Built the panoramic training data needed for modeling from scratch. Within a ~100M KRW budget,
    compared building vs. buying — sampled and statistically analyzed candidate purchase data,
    judged it unsuitable, and concluded to build in-house. Turned ~20,000-30,000 raw images into
    ~4,000 training images via a selection pipeline, and built a custom Windows annotation tool with
    an embedded medical SAM, security, and log tracking. Documented labeling guidelines and trained
    8 specialists and 5 dental technicians/hygienists.
---

## 1. 문제 정의와 제약조건
- 제품 요구사항이 불명확한 상태에서 모델링에 필요한 파노라마 학습 데이터를 처음부터 정의·구축
- 원내 데이터 반출 제약 (상용 툴·외부 반출 제한)
- '무엇을 어떻게 라벨링할지' 체계 자체를 정립

## 2. 접근과 대안 비교

| 대안 | 장점 | 탈락 / 채택 사유 |
|---|---|---|
| 외부 데이터 매입 | 빠른 확보 | 샘플링·통계 분석 결과 라벨 품질 등이 부적합 → 매입 안 함 |
| 상용/오픈소스 라벨링 툴 | 즉시 사용 | 라벨링 목적에 기능이 부적합 → 코드를 참고해 커스텀 개발 |
| **채택: 자체 데이터 구축 + 커스텀 툴** | 목적 적합·보안 확보 | 비용·시간 감수 |

## 3. 구현
- **데이터 파이프라인**: 파노라마 원본 약 2~3만 장을 획득 → 선별 기준·자동화 파이프라인으로 학습용
  약 4,000장을 구축 → QC → DB → 자동 재학습
- **커스텀 툴 (Windows)**: medical SAM 탑재, 라벨 자유 편집, 논의가 필요한 객체 표시, 검수 모아보기,
  라벨 항목 누락 방지 UX
- **보안·운영**: 자사 데이터·라벨 유출 방지, 로그인 서버, 사용자 로그 트래킹 기반 퍼포먼스 모니터링
- **라벨링 SAM**: 치아 분할용 SAM을 파인튜닝해 탑재 (p13 참조)
- 기획·개발·유지보수·사용법 교육·자료 제작 전 과정을 단독으로 진행; 참고한 오픈소스 툴에 기능을 기여(contribute)

## 4. 라벨 운영
- 라벨링·검수 기준을 문서화
- 대학병원 전문의 8명과 치기공사·위생사 5인을 교육·온보딩·관리, 외주 작업자를 다회 교육

## 5. 결과
- 학습용 파노라마 데이터 약 4,000장을 구축해 후속 프로젝트에 재사용
- 오픈소스 라벨링 툴에 유용한 기능을 기여

## 6. 난이도 · 한계
- 요구사항이 불명확하고 아무도 해보지 않은 새 영역을 체계·툴·전처리까지 scratch에서 주도
