---
id: p05
title_ko: "Cephalometric 랜드마크 검출 모델링"
title_en: "Cephalometric Landmark Detection"
org: "Genoray"
period: "2025-02 ~ 2025-07"
role: "리드"
role_note_ko: "단독 개발"
role_note_en: "Solo development"
tags: ["Medical AI", "Vision", "Detection", "On-device"]
angles: [modeling-foundation, performance-optimization, stakeholder-alignment]

problem:
  goal_ko: "치과 cephalometric 영상에서 교정 진단용 해부학적 랜드마크 42개를 자동 검출하는 모델 구축"
  goal_en: "Build a model that auto-detects 42 anatomical landmarks for orthodontic diagnosis on dental cephalometric images."
  hurdle_ko: |
    - '정확한' 랜드마크 위치 자체가 의사·영상마다 이견이 커 GT 정의가 어려움
    - 학습 데이터 부족·라벨 일관성 문제로 성능이 정체됨
    - 2D 영상 특성상 구조물이 겹쳐 일부 랜드마크를 단일 위치로 특정하기 어려움
  hurdle_en: |
    - The 'correct' landmark location itself varies across doctors and images, making GT hard to define
    - Performance plateaued due to limited data and label inconsistency
    - In 2D images, overlapping structures make some landmarks hard to pin to a single point

role_groups:
  - label_ko: "Cephalometric 랜드마크 42개 검출 모델을 설계·학습"
    label_en: "Designed and trained a 42-landmark detection model"
    uses: [f1, f2]
  - label_ko: "데이터 부족·라벨 일관성에 따른 성능 정체를 돌파"
    label_en: "Broke through the plateau caused by limited data and label inconsistency"
    uses: [f3, f4]
  - label_ko: "임상 자문의 4인과 타사 벤치마킹을 통해 모델의 정확도·임상 유의성을 확보"
    label_en: "Secured accuracy and clinical significance via clinical advisors and competitor benchmarking"
    uses: [f5]
  - label_ko: "학습 모델을 C++·DLL로 패키징해 앱 개발팀에 이관"
    label_en: "Packaged the trained model as C++/DLL and handed it to the app team"
    uses: [f6]

facts:
  f1: {kind: artifact, value_ko: "랜드마크 42개를 검출하는 keypoint detection 모델 개발 및 최적화", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "Heatmap 기반 voting과 HRNet 백본 CNN 구조로 랜드마크 검출 모델을 설계", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "성능 정체의 원인을 데이터 부족·특정 랜드마크 라벨 바일관성에 의한 것으로 정의", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "다양한 학습·증강 기법 실험을 실험하고, 추가 데이터 확보를 통해 성능 정체 돌파", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "'정확한' 랜드마크 위치를 두고 의사·영상 간 이견이 큰 태스크 — 임상 자문의 2인과 타사 결과 분석을 통해 GT 정확도·임상적 유의성을 확보", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "학습한 랜드마크 검출 모델을 C++ 변환·DLL 패키징 후 애플리케이션 개발팀에 이관", value_en: "Converted the trained landmark-detection model to C++, packaged it as a DLL, and handed it to the app team", disclosure: public, confidence: measured}
  f7: {kind: metric, value_ko: "평균 방사 오차(MRE) 1.21mm 이내, SDR@2mm 80% 달성", value_en: "Achieved mean radial error (MRE) within 1.21mm and SDR@2mm of 80%", disclosure: public, confidence: measured}

variants:
  - angle: modeling-foundation
    uses: [f1, f2, f4]
    ko: "치과 cephalometric 랜드마크 42개 검출 모델을 Heatmap voting·HRNet 백본으로 설계·학습하고, 데이터 부족·라벨 일관성에 따른 성능 정체를 증강·추가 데이터로 돌파"
    en: "Designed and trained a 42-landmark cephalometric detection model with heatmap voting and an HRNet backbone, breaking a data/label-consistency plateau via augmentation and additional data"
  - angle: performance-optimization
    uses: [f7]
    ko: "평균 방사 오차(MRE) 1.21mm 이내, SDR@2mm 80% 달성"
    en: "Achieved mean radial error (MRE) within 1.21mm and SDR@2mm of 80%"
  - angle: stakeholder-alignment
    uses: [f5]
    ko: "'정확한' 위치에 이견이 큰 태스크에서 임상 자문의 2인·타사 결과 분석으로 GT 정확도와 임상적 유의성을 확보"
    en: "On a task with wide disagreement over the 'correct' location, secured GT accuracy and clinical significance via 2 clinical advisors and competitor analysis"

short:
  ko: "치과 cephalometric 랜드마크 42개 검출 모델을 Heatmap voting·HRNet 백본으로 설계·학습하고, 데이터 부족·라벨 일관성에 따른 성능 정체를 증강·추가 데이터로 돌파"
  en: "Designed and trained a 42-landmark cephalometric detection model with heatmap voting and an HRNet backbone, breaking a data/label-consistency plateau via augmentation and additional data"
---
