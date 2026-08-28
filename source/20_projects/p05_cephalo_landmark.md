---
id: p05
title_ko: Cephalometric 교정 랜드마크 검출 (42개)
title_en: Cephalometric Orthodontic Landmark Detection (42 points)
org: Genoray
period: 2025-02 ~ 2025-07
role: "모델 개발 단독 (기획팀·타부서와 긴밀 협업)"
tags: [Medical-AI, Vision, On-device]
angles: [modeling-foundation, shipping-delivery, research-depth]

card:
  ko: "정답 위치조차 의사마다 갈리는 난제에서 교정 랜드마크 42개 검출 모델을 설계"
  en: "Built a 42-landmark detector despite contested ground-truth positions"

problem:
  goal_ko: "치과 cephalometric 영상에서 교정 진단용 해부학적 랜드마크 42개를 자동 검출하는 모델 구축"
  goal_en: "Build a detector that automatically locates the 42 orthodontic anatomical landmarks used for diagnosis on dental cephalometric images."
  hurdle_ko: |
    - '정확한' 랜드마크 위치 자체가 의사·영상마다 이견이 커 GT 정의가 어려움
    - 학습 데이터 부족·라벨 일관성 문제로 성능이 정체됨
    - 2D 영상 특성상 구조물이 겹쳐 일부 랜드마크를 단일 위치로 특정하기 어려움
  hurdle_en: |
    - The 'correct' landmark position is contested across clinicians and images, so GT is hard to define
    - Performance stalled due to data scarcity and label inconsistency
    - In 2D images, overlapping structures make some landmarks hard to pin to a single point

role_groups:
  - label_ko: "cephalometric 랜드마크 42개 검출 모델을 설계·학습"
    label_en: "Designed and trained the 42-point cephalometric landmark detector"
    uses: [f1, f3]
  - label_ko: "임상 자문의 4인과 조율해 GT 정확도·임상 유의성을 확보"
    label_en: "Aligned with 4 clinical advisors to secure GT accuracy and clinical validity"
    uses: [f5]
  - label_ko: "데이터 부족·라벨 일관성에 따른 성능 정체를 돌파"
    label_en: "Broke through the performance plateau from data scarcity and label inconsistency"
    uses: [f6]
  - label_ko: "학습 모델을 C++·DLL로 패키징해 앱 개발팀에 이관"
    label_en: "Packaged the trained model as C++/DLL and handed off to the app team"
    uses: [f2]

facts:
  f1: {kind: scope, value_ko: "Dental cephalometric 영상에서 해부학적 교정 랜드마크 42개를 검출하는 keypoint detection 모델", value_en: "a keypoint detection model locating 42 orthodontic anatomical landmarks on dental cephalometric images", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "학습한 랜드마크 검출 모델을 C++ 변환·DLL 패키징 후 애플리케이션 개발팀에 이관", value_en: "converted the trained landmark model to C++ and packaged it as a DLL, handed off to the application development team", disclosure: public, confidence: measured}
  f3: {kind: decision, value_ko: "heatmap 기반 voting과 HRNet 백본 CNN 구조로 랜드마크 검출 모델을 설계", value_en: "designed the landmark detector as heatmap-based voting on an HRNet-backbone CNN", disclosure: public, confidence: measured}
  f4: {kind: metric, value_ko: "평균 방사 오차(MRE) 1.21mm 이내, SDR@2mm 80% 달성", value_en: "achieved a mean radial error (MRE) within 1.21mm and 80% SDR@2mm", disclosure: public, confidence: measured}
  f5: {kind: decision, value_ko: "'정확한' 랜드마크 위치를 두고 의사·영상 간 이견이 큰 태스크 — 임상 자문의 4인과 조율로 GT 정확도·임상적 유의성을 확보", value_en: "Because the 'correct' landmark position is inherently contested across clinicians and images, secured GT accuracy and clinical validity through iterative alignment with 4 clinical advisors", disclosure: public, confidence: measured}
  f6: {kind: decision, value_ko: "데이터 부족·라벨 일관성에 따른 성능 정체를 다양한 기법 실험·데이터 정확도 개선으로 돌파", value_en: "broke through a performance plateau caused by data scarcity and label inconsistency by experimenting with multiple techniques and improving data accuracy", disclosure: public, confidence: measured}
  # 학습 데이터 구축·운영은 p12 참조

variants:
  - angle: modeling-foundation
    uses: [f3, f4]
    ko: "heatmap 기반 voting과 HRNet 백본 CNN으로 랜드마크 검출 모델을 설계해 평균 오차(MRE) 1.21mm 이내·SDR@2mm 80% 달성"
    en: "Designed the landmark detector as heatmap-based voting on an HRNet backbone, achieving MRE within 1.21mm and 80% SDR@2mm"
  - angle: modeling-foundation
    uses: [f1]
    ko: "Dental cephalometric 영상에서 교정 해부학 랜드마크 42개를 찾는 keypoint detection 모델을 설계·학습"
    en: "Designed and trained a keypoint detection model locating 42 orthodontic anatomical landmarks on dental cephalometric images"
  - angle: research-depth
    uses: [f6]
    ko: "데이터 부족·라벨 일관성에 따른 성능 정체 구간을 다양한 기법 실험·데이터 정확도 개선으로 돌파"
    en: "Broke through a performance plateau caused by data scarcity and label inconsistency by experimenting with multiple techniques and improving data accuracy"
  - angle: shipping-delivery
    uses: [f2]
    ko: "학습한 랜드마크 검출 모델을 C++ 변환·DLL 패키징해 애플리케이션 개발팀에 이관"
    en: "Converted the trained landmark model to C++, packaged it as a DLL, and handed it off to the application development team"

short:
  ko: >
    Dental cephalometric 영상에서 교정 진단용 해부학적 랜드마크 42개를 찾는 keypoint detection
    모델(heatmap 기반 voting, HRNet 백본). 임상 자문의 4인과 조율로 임상적으로 유의한 품질을
    확보하고, 평균 오차(MRE) 1.21mm 이내·SDR@2mm 80% 달성. 학습 모델은 C++ 변환·DLL
    패키징 후 애플리케이션 개발팀에 이관.
  en: >
    A keypoint detection model (heatmap-based voting, HRNet backbone) locating 42 orthodontic
    anatomical landmarks on dental cephalometric images. Aligned with 4 clinical advisors to reach
    clinically meaningful quality — MRE within 1.21mm and 80% SDR@2mm. The trained model was
    converted to C++, packaged as a DLL, and handed off to the application development team.
---

## 1. 문제 정의와 제약조건
- Dental cephalometric 영상에서 교정 진단에 쓰이는 해부학적 랜드마크 42개를 자동 검출
- 제약: **'정확한' 랜드마크 위치 자체가 의사·영상마다 이견**이 큰 태스크 → GT 정의가 어려움
- 데이터 부족·라벨 일관성 문제

## 2. 접근과 대안 비교
- 채택: **heatmap 기반 voting + HRNet 백본 CNN** 구조
- 태스크 특성상 좌표를 하나로 회귀하기보다 heatmap으로 위치 분포를 추정하는 방식이 적합

## 3. 구현
- heatmap 기반 voting, HRNet 백본
- 학습 데이터 구축·운영은 **p12** 참조
- 공개 구현(동일 태스크 파이프라인, 개인·데이터 미포함): https://github.com/lovejoohero0228/cephalometric-landmark-detection

## 4. 검증
- 지표: 평균 방사 오차(MRE), SDR@2mm
- 결과: MRE 1.21mm 이내, SDR@2mm 80%
- 임상 자문의 4인과 조율로 임상적 유의성 확보

## 5. 결과
- 임상적으로 유의한 수준의 품질 달성 (MRE 1.21mm 이내, SDR@2mm 80%)
- 데이터 부족·라벨 일관성에 따른 성능 정체를 기법 실험·데이터 정확도 개선·임상 소통으로 돌파

## 6. 한계
- 2D 영상 특성상 구조물이 겹쳐, 일부 랜드마크를 단일 위치로 특정하기 어려움
