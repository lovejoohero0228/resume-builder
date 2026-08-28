---
id: p14
title_ko: 의료영상 비식별화 OCR
title_en: Medical Image De-identification OCR
org: Genoray
period: 2026-04
role: 단독
tags: [Medical-AI, Vision]
angles: [engineering-craft]

card:
  ko: "위치·형식이 제각각인 번인 텍스트에서 환자 민감정보를 OCR로 자동 비식별화"
  en: "OCR de-identification of burned-in patient info across varied layouts"

problem:
  goal_ko: "영상에 번인(burn-in)된 병원 정보·환자 정보·ID 등 민감정보를 자동으로 비식별화"
  goal_en: "Automatically de-identify sensitive information burned into images — hospital info, patient info, IDs."
  hurdle_ko: |
    - 영상에 텍스트가 번인되어 위치·형식이 제각각
    - 스캔본 영상에서는 정확히 걸러내지 못하는 한계
  hurdle_en: |
    - Text is burned into images, so its position and format vary widely
    - Accuracy is limited on scanned images, where it tends to miss

role_groups:
  - label_ko: "민감정보를 비식별화하는 OCR 처리를 구현"
    label_en: "Built the OCR-based de-identification processing"
    uses: [f1, f2]

facts:
  f1: {kind: artifact, value_ko: "영상에 포함된 병원 정보·환자 정보·ID 등 민감정보를 비식별화하는 OCR 기반 처리를 구현", value_en: "OCR-based processing to de-identify sensitive information embedded in images — hospital info, patient info, IDs", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "기성 OCR 엔진·라이브러리·오픈소스 모델을 조합해 구현", value_en: "built by combining off-the-shelf OCR engines, libraries, and open-source models", disclosure: public, confidence: measured}

variants:
  - angle: engineering-craft
    uses: [f1, f2]
    ko: "영상에 포함된 병원·환자 정보·ID 등 민감정보를 기성 OCR 엔진·라이브러리·오픈소스 모델을 조합해 비식별화"
    en: "De-identified sensitive information (hospital, patient, ID) embedded in images by combining off-the-shelf OCR engines, libraries, and open-source models"

short:
  ko: >
    영상에 포함된 병원·환자 정보·ID 등 민감정보를 비식별화하기 위한 OCR 기반 처리 (소규모).
    기성 OCR 엔진·라이브러리·오픈소스 모델을 조합해 구현.
  en: >
    OCR-based processing to de-identify sensitive information (hospital, patient, ID) embedded in
    images (small scope), built by combining off-the-shelf OCR engines, libraries, and open-source models.
---

## 1. 문제 정의
- 영상에 번인(burn-in)된 병원 정보·환자 정보·ID 등 민감정보를 비식별화

## 2. 구현
- 기성 OCR 엔진·라이브러리·오픈소스 모델을 조합해 구성

## 3. 한계
- 스캔본 영상에서는 정확히 걸러내지 못하는 경향
