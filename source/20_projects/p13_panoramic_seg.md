---
id: p13
title_ko: "Dental Panoramic Radiograph 부위·병변 분할 모델링"
title_en: "Dental Panoramic Radiograph Segmentation"
org: "Genoray"
period: "2025-08 ~ 2026-10"
role: "리드"
role_note_ko: "팀원 1명과 협업"
role_note_en: "With one teammate"
tags: ["Medical AI", "Vision", "Segmentation", "Detection", "On-device"]
angles: [ownership-e2e, modeling-foundation, shipping-delivery]

problem:
  goal_ko: "치과 파노라마에서 해부 구조·보철물·병변을 자동 인식하는 판독 보조 모델을 개발해 진료 효율을 높이는 것"
  goal_en: "Develop a reading-assist model that auto-recognizes anatomy, prostheses, and lesions on dental panoramic X-rays to improve clinical efficiency."
  hurdle_ko: |
    - 제품 기획·목표 수준·학습 데이터 구축까지 처음부터 정립 필요
    - 개발 목표 모델이 많고 복잡 (구조·보철물·병변 19여 종)
    - 병변과 일부 해부학적 부위는 '정답 라벨’에 대한 의사·영상별 이견이 커 GT 정의가 어려움
  hurdle_en: |
    - Everything from product planning and target level to training-data construction had to be established from scratch
    - Many and complex target models (19+ kinds of structures, prostheses, lesions)
    - For lesions and some anatomy, doctors and images disagree on the 'correct label', making GT hard to define

role_groups:
  - label_ko: "제품 기획·목표·데이터 구축부터 제품화까지 파노라마 모델을 end-to-end로 리드"
    label_en: "Led the panoramic model end to end — from product planning, targets, and data construction through productization"
    uses: [f1, f2]
  - label_ko: "19여 종의 구조·보철물·병변 항목들을 10여 개 모델로 묶어, 각각 ablation 실험을 통해 품질·성능을 최적화"
    label_en: "Grouped 19+ items into ~10 models and optimized each via ablation experiments"
    uses: [f3, f4, f5]
  - label_ko: "임상의 자문 미팅을 준비하고 진행하며 전문가의 피드백을 효과적으로 활용할 수 있도록 개발 리드"
    label_en: "Prepared and ran clinical advisory meetings, leading development to use expert feedback effectively"
    uses: [f6]
  - label_ko: "학습 모델을 C++·DLL로 패키징해 앱 개발팀에 이관"
    label_en: "Packaged the trained model as C++/DLL and handed it to the app team"
    uses: [f7]

facts:
  f1: {kind: artifact, value_ko: "제품 기획, 목표 수준 설정, 학습 데이터 구축부터 제품화까지 파노라마 모델 개발을 scratch에서부터 end-to-end로 관여", value_en: "Led panoramic-model development end to end from scratch — product planning, target-setting, and training-data construction through productization", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "본 AI 기능의 임상적·제품적 의미를 이해하고, 유의미한 제품 개발을 위한 의견 조율  예. 병변을 마스크로 정의하는 것의 모순을 임상의와의 자문을 통해 기획팀에 의견 전달", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "치과 파노라마 x-ray 영상에서 치아(Tooth)·상악동(sinus)·하치조신경관(IAC)·치조정(Alveolar crest)·CEJ·보철물(Prosthesis)·악관절(TMJ)과 우식증(Caries)·치주염(periodontitis)·매복치(Impaction·기타 병변(Lesion) 탐지 등 10여 개 모델을 개발", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "분할은 Mask2Former·MaskDINO(트랜스포머)와 U-Net(전통)으로, 검출은 YOLO·Detectron2·MMDetection 등 다양한 프레임워크로 실험", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "모델 구분과 task 통합을 다수의 ablation 실험으로 비교해 최적 구성을 도출", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "매 달 1회의 자문 미팅을 진행하며, 모델링 기획 단계부터 개발 현황을 효과적으로 공유하고 피드백 반영 싸이클 진행", value_en: "", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "학습 모델을 C++로 변환하고 DLL로 패키징해 애플리케이션 개발팀에 이관", value_en: "", disclosure: public, confidence: measured}
  f8: {kind: adoption, value_ko: "임상의 2인의 정성적 평가를 통해 임상적으로 유의한 10종 모델 개발", value_en: "Developed 10 clinically meaningful models, validated by qualitative review from 2 clinicians", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1]
    ko: "치과 파노라마 판독 보조 모델을 제품 기획·목표·학습 데이터 구축부터 제품화까지 end-to-end로 리드"
    en: "Led a dental-panoramic reading-assist model end to end — from product planning, targets, and training-data construction through productization"
  - angle: modeling-foundation
    uses: [f3, f4, f5]
    ko: "여러 종의 구조·보철물·병변을 10여 개 모델로 묶고, 분할(Mask2Former·MaskDINO·U-Net)과 검출(YOLO·Detectron2·MMDetection)을 ablation 실험으로 비교해 최적 구성을 도출"
    en: "Grouped structures, prostheses, and lesions into ~10 models and derived the optimal setup via ablation — segmentation (Mask2Former, MaskDINO, U-Net) vs detection (YOLO, Detectron2, MMDetection)"
  - angle: shipping-delivery
    uses: [f8, f7]
    ko: "임상의 2인의 정성 평가로 임상적으로 유의한 10종 모델을 개발하고, 학습 모델을 C++·DLL로 패키징해 앱 개발팀에 이관"
    en: "Developed 10 clinically meaningful models validated by 2 clinicians, and packaged the trained models as C++/DLL for the app team"

short:
  ko: "치과 파노라마 판독 보조 모델을 제품 기획·목표·학습 데이터 구축부터 제품화까지 end-to-end로 리드"
  en: "Led a dental-panoramic reading-assist model end to end — from product planning, targets, and training-data construction through productization"
---
