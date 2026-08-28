---
id: p10
title_ko: 하이브리드 게시글 추천 시스템 (AI 바우처)
title_en: Hybrid Listing Recommender (AI Voucher Project)
org: Dfinite
period: 2025-01
role: 단독
tags: [Enterprise-AI]
angles: [ownership-e2e, engineering-craft, research-depth]

card:
  ko: "정답 지표가 없는 조건에서 장비 메타데이터만으로 게시글 추천 시스템을 단독 설계"
  en: "Solo recommender from metadata alone, with no target metric"

problem:
  goal_ko: "중고 산업 장비 거래 플랫폼의 판매 게시글 추천 시스템을 AI 바우처 과제로 단독 구축."
  goal_en: "Solo-build a listing recommender for a used industrial-equipment marketplace as an AI Voucher project."
  hurdle_ko: |
    - 목표 지표가 없어 성능·품질을 정량으로 검증하기 어려움
    - 상품·장비 메타데이터(시리얼·제조사·연식 등)만으로 유사도를 설계해야 함
  hurdle_en: |
    - No target metric was set, making quantitative validation of performance/quality hard
    - Similarity had to be designed from item/equipment metadata alone (serial, manufacturer, model year, …)

role_groups:
  - label_ko: "판매 게시글 추천 시스템을 단독으로 설계·개발"
    label_en: "Solo-designed and built the listing recommender"
    uses: [f1]
  - label_ko: "콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드 추천기를 구현"
    label_en: "Built a hybrid content-based + collaborative-filtering recommender"
    uses: [f2]
  - label_ko: "로그의 사용 분포 분석과 통계 가정으로 추천 방식을 설계"
    label_en: "Designed the recommender from log-based usage analysis and statistical assumptions"
    uses: [f3]
  - label_ko: "목표 지표가 없는 가운데 고객사와 소통하며 점진 개선"
    label_en: "Improved iteratively with the client despite the absence of a target metric"
    uses: [f4]

facts:
  f1: {kind: artifact, value_ko: "AI 바우처 사업 과제로 중고 산업 장비 거래 플랫폼의 판매 게시글 추천 시스템을 단독으로 설계·개발", value_en: "solo-designed and built a listing recommender for a used industrial-equipment marketplace as an AI Voucher project", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "상품정보·장비 시리얼넘버·제조사·제조국가·가격대·연식 등을 기반으로 콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드를 채택", value_en: "adopted a hybrid of content-based filtering and collaborative filtering, using item info such as serial number, manufacturer, country of manufacture, price range, and model year", disclosure: public, confidence: measured}
  f3: {kind: decision, value_ko: "로그 분석으로 사용 분포를 파악하고 여러 통계 가정을 수립해 추천 방식을 설계", value_en: "analyzed usage distribution from logs and designed the recommender under several statistical assumptions", disclosure: public, confidence: measured}
  f4: {kind: decision, value_ko: "목표 지표가 없어 성능·품질을 정량으로 검증하기 어려운 조건에서 고객사와 소통하며 점진 개선", value_en: "with no target metric making quantitative validation hard, improved iteratively through communication with the client", disclosure: public, confidence: measured}
  f5: {kind: adoption, value_ko: "PoC를 진행한 뒤 고객사 이관까지 완료", value_en: "ran the PoC and completed handoff to the client", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1, f5]
    ko: "AI 바우처 과제로 중고 산업 장비 거래 플랫폼의 판매 게시글 추천 시스템을 단독으로 설계·개발하고, PoC 후 이관까지 완료"
    en: "As an AI Voucher project, solo-designed and built a listing recommender for a used industrial-equipment marketplace and completed PoC and handoff"
  - angle: engineering-craft
    uses: [f2]
    ko: "상품정보·시리얼넘버·제조사·제조국가·가격대·연식 등을 기반으로 콘텐츠 기반 필터링과 협업 필터링을 결합한 하이브리드 추천기를 구현"
    en: "Built a hybrid recommender combining content-based and collaborative filtering over item info — serial number, manufacturer, country, price range, model year"
  - angle: research-depth
    uses: [f3]
    ko: "로그 기반 사용 분포 분석과 여러 통계 가정 수립으로 추천 방식을 설계"
    en: "Designed the recommender from log-based usage-distribution analysis and several statistical assumptions"

short:
  ko: >
    중고 산업 장비 거래 플랫폼의 판매 게시글 추천 시스템을 AI 바우처 과제로 단독 설계·개발.
    상품정보·시리얼넘버·제조사·제조국가·가격대·연식 등을 기반으로 콘텐츠 기반 필터링과 협업 필터링을
    하이브리드로 결합하고, 로그의 사용 분포 분석과 통계 가정으로 설계. 목표 지표가 없어 고객사와 소통하며
    점진 개선하고, PoC 후 이관까지 완료.
  en: >
    Solo-built a listing recommender for a used industrial-equipment marketplace as an AI Voucher
    project. Combined content-based and collaborative filtering over item info (serial number,
    manufacturer, country, price range, model year), designed from log-based usage-distribution
    analysis and statistical assumptions. With no target metric, improved iteratively with the
    client and completed PoC and handoff.
---

## 1. 문제 정의와 제약조건
- AI 바우처 사업 과제 — 중고 산업 장비 거래 플랫폼의 **판매 게시글 추천**
- 목표 지표가 없어 성능·품질을 정량으로 검증하기 어려운 조건

## 2. 접근과 구현
- 상품정보·장비 시리얼넘버·제조사·제조국가·가격대·연식 등을 피처로 활용
- **콘텐츠 기반 필터링 + 협업 필터링 하이브리드**
- 로그 분석으로 사용 분포를 파악하고 여러 통계 가정을 수립해 설계

## 3. 결과 · 한계
- 고객사와 소통하며 점진 개선 — **PoC 진행 후 이관 완료**
- **한계**: 목표 지표가 없어 정량 검증이 곤란
