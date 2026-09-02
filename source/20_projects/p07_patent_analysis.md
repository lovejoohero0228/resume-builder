---
id: p07
title_ko: 특허 분석
title_en: Patent Analysis
org: Genoray
period: 2026-04 ~ 2026-08
role: 참여 (팀)
tags: [Medical-AI]
angles: [shipping-delivery, stakeholder-alignment]

card:
  ko: "특허 300건 이상을 AI 관점 유사성으로 검토해 개발 방향·IP 리스크 판단 근거 마련"
  en: "Reviewed 300+ patents by AI-level similarity to guide direction & IP"

problem:
  goal_ko: "C-arm 신규 선행 기술과 2D Ceph 특허 지형을 파악해 개발 방향·IP 리스크 정리"
  goal_en: "Map the C-arm new-prior-art and 2D-Ceph patent landscape to inform development direction and IP risk."
  hurdle_ko: |
    - 외부 특허 300건 이상을 검토·등급화해야 하는 대량 작업
    - AI 관점의 기술 유사성으로 침해 여부를 판단해야 함
    - 외부 변리사·임상 자문·TF팀 등 다자 협업 조율
  hurdle_en: |
    - Large-scale review and grading of 300+ external patents
    - Infringement had to be judged by AI-level technical similarity
    - Multi-party coordination with outside patent counsel, clinical advisors, and the TF team

role_groups:
  - label_ko: "C-arm·2D Ceph 관련 외부 특허 300건 이상을 검토·등급화하고 침해 여부를 판단"
    label_en: "Reviewed and graded 300+ external patents and judged infringement"
    uses: [f1, f2]
  - label_ko: "임상 자문·TF와 함께 C-arm 선행 기술 테크트리를 기능별로 직접 작성"
    label_en: "Built the C-arm prior-art technology tree by function with clinical advisors and the TF team"
    uses: [f3]
  - label_ko: "외부 변리사 특허사무소와 협업해 분석을 수행"
    label_en: "Ran the analysis in collaboration with an outside patent-attorney firm"
    uses: [f4]

facts:
  f1: {kind: scope, value_ko: "C-arm 신규 선행 기술·2D Ceph 관련 외부 특허 300건 이상을 검토·등급화", value_en: "reviewed and graded 300+ external patents related to C-arm new prior art and 2D cephalometric technology", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "AI 관점의 기술 유사성으로 침해 여부를 판단하고, 벤치마킹 가능한 내용을 상세 검토 대상으로 선별", value_en: "judged infringement by AI-level technical similarity and flagged benchmarkable content for detailed review", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "임상 자문·TF팀 회의를 거쳐 C-arm 선행 기술 테크트리를 기능별로 직접 작성", value_en: "built the C-arm prior-art technology tree by function, through clinical-advisory and TF-team sessions", disclosure: public, confidence: measured}
  f4: {kind: decision, value_ko: "외부 변리사 특허사무소와 협업해 분석을 진행", value_en: "worked with an outside patent-attorney firm on the analysis", disclosure: public, confidence: measured}
  f5: {kind: adoption, value_ko: "분석 결과를 개발 방향 결정·회피 설계 검토·신규 IP 출원에 반영", value_en: "the analysis fed into development-direction decisions, design-around review, and new IP filings", disclosure: public, confidence: measured}

variants:
  - angle: shipping-delivery
    uses: [f5]
    ko: "특허 분석 결과를 개발 방향 결정·회피 설계 검토·신규 IP 출원에 반영"
    en: "Fed the patent analysis into development-direction decisions, design-around review, and new IP filings"
  - angle: stakeholder-alignment
    uses: [f4, f3]
    ko: "외부 변리사·임상 자문·TF팀과 협업해 C-arm 선행 기술 테크트리를 직접 작성"
    en: "Worked with outside patent counsel, clinical advisors, and the TF team to build the C-arm prior-art technology tree"

short:
  ko: >
    C-arm 신규 선행 기술·2D Ceph 관련 외부 특허 300건 이상을 AI 관점의 기술 유사성으로
    침해 여부를 판단하고 벤치마킹 대상을 선별. 임상 자문·TF팀 회의를 거쳐 C-arm 선행 기술
    테크트리를 직접 작성. 외부 변리사와 협업했으며, 분석 결과는 개발 방향 결정·회피 설계·신규 IP 출원에 반영.
  en: >
    Reviewed and graded 300+ external patents on C-arm new prior art and 2D cephalometric tech,
    judging infringement by AI-level technical similarity and flagging benchmarkable content. Built
    the C-arm prior-art technology tree via clinical-advisory and TF sessions, worked with outside
    patent counsel, and fed the results into development direction, design-around, and new IP filings.
---

## 1. 문제 정의
- C-arm 신규 선행 기술·2D Ceph 관련 특허 지형을 파악해 개발 방향·IP 리스크를 정리
- 외부 변리사 특허사무소와 협업

## 2. 한 일
- AI 관점의 기술 유사성으로 특허 300건 이상의 침해 여부를 판단하고, 벤치마킹 대상을 상세 검토 대상으로 선별
- 임상 자문·TF팀 회의를 거쳐 C-arm 선행 기술 테크트리를 기능별로 직접 작성
- (덴탈 과제는 제품 기획이 확정된 상태로, 타부서에서 준비 중)

## 3. 결과 · 영향
- 분석 결과를 개발 방향 결정·회피 설계안 검토·신규 IP 출원에 반영

## 4. 메모
- 타사 기술의 유사성·차이를 파악하는 과정에서 다수의 벤치마킹 아이디어를 확보
