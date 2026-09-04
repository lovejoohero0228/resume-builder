---
id: p10
title_ko: "중고 거래 플랫폼 하이브리드 추천 시스템"
title_en: "Used-Trade Platform Hybrid Recommendation System"
org: "Dfinite"
period: "2024-10"
role: "리드"
role_note_ko: "단독 개발"
role_note_en: "Solo development"
tags: ["Recommendation"]
angles: [ownership-e2e, engineering-craft]

problem:
  goal_ko: "중고 산업 장비 거래 플랫폼의 판매 게시글 추천 시스템을 AI 바우처 과제로 단독 구축"
  goal_en: "Solo-build a sales-listing recommendation system for a used industrial-equipment trading platform as an AI-voucher project."
  hurdle_ko: |
    - 목표 지표가 없어 성능·품질을 정량으로 검증하기 어려움
    - 신규 시스템을 개발하는 건으로 cold-start 문제가 있었고, 관련 로그 데이터와 장비 메타데이터만으로 유사도를 설계해야 함
  hurdle_en: |
    - No target metric, so quality/performance was hard to verify quantitatively
    - A new system with a cold-start problem — similarity had to be designed from only log data and equipment metadata

role_groups:
  - label_ko: "콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드 추천기를 구현"
    label_en: "Built a hybrid recommender combining content-based and collaborative filtering"
    uses: [f1, f2]
  - label_ko: "목표 지표가 없는 가운데 고객사와 소통하며 점진 개선"
    label_en: "Iterated with the client despite no target metric"
    uses: [f3]

facts:
  f1: {kind: artifact, value_ko: "상품정보·장비 시리얼넘버·제조사·제조국가·가격대·연식 등을 기반으로 콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드를 채택", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "로그 분석으로 사용 분포를 파악하고 여러 통계 가정을 수립해 추천 방식을 설계", value_en: "Analyzed logs to understand usage distribution and set statistical assumptions to design the recommendation approach", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "목표 지표가 없어 성능·품질을 정량으로 검증하기 어려운 조건에서 고객사와 소통하며 점진 개선", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: adoption, value_ko: "PoC 개발을 완료한 뒤, 고객사 이관까지 완료하며 과제 완수", value_en: "Completed the PoC and handed it over to the client, finishing the project", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1, f4]
    ko: "중고 산업장비 거래 플랫폼의 게시글 추천 시스템을 AI 바우처 과제로 단독 구축하고, 고객사 이관까지 완료해 과제를 완수"
    en: "Solo-built a listing recommendation system for a used industrial-equipment platform as an AI-voucher project and handed it off to the client"
  - angle: engineering-craft
    uses: [f1, f2]
    ko: "콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드 추천기를 구현 — cold-start 조건에서 로그·장비 메타데이터 유사도로 설계"
    en: "Built a hybrid recommender combining content-based and collaborative filtering — designed from log and equipment-metadata similarity under cold-start"

short:
  ko: "중고 산업장비 거래 플랫폼의 게시글 추천 시스템을 AI 바우처 과제로 단독 구축하고, 고객사 이관까지 완료해 과제를 완수"
  en: "Solo-built a listing recommendation system for a used industrial-equipment platform as an AI-voucher project and handed it off to the client"
---
