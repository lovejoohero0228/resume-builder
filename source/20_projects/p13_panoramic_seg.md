---
id: p13
title_ko: Panoramic 구조물·병변 분할·검출 (10여 개 모델)
title_en: Panoramic Structure & Lesion Segmentation / Detection
org: Genoray
period: 2025-08 ~ 2026-10
role: "리드 (중반 이후 팀원 1명 충원)"
tags: [Medical-AI, Vision, On-device, LLM, Multimodal]
angles: [ownership-e2e, modeling-foundation, stakeholder-alignment]

card:
  ko: "병변 정답조차 모순인 난제에서 판독 보조 모델 10여 개를 기획·제품화까지 리드"
  en: "Led ~10 panoramic reading models despite contradictory lesion ground truth"

problem:
  goal_ko: "치과 파노라마에서 해부 구조·보철물·병변을 자동 인식하는 판독 보조 모델을 개발해, 경쟁 제품이 제공하는 범위를 모두 커버"
  goal_en: "Build a suite of dental-panoramic reading-assist models that auto-recognize anatomy, prosthetics, and lesions — covering everything the competitor product offers."
  hurdle_ko: |
    - 인식 대상이 많고 복잡 (구조·보철물·병변 10여 종)
    - 병변은 '정확한' 마스크 정답을 만드는 것 자체에 모순이 있음
    - 제품 기획·목표 수준·학습 데이터까지 처음부터 정립 필요
  hurdle_en: |
    - Many, complex target items (~10 kinds of structures/prosthetics/lesions)
    - For lesions, a 'precise' mask ground truth is inherently contradictory
    - Had to establish product planning, target levels, and the dataset from scratch

role_groups:
  - label_ko: "제품 기획·목표·데이터부터 제품화까지 파노라마 모델을 end-to-end로 리드"
    label_en: "Led panoramic model development end to end — from planning and data to productization"
    uses: [f9]
  - label_ko: "구조·보철물 분할과 병변 탐지 10여 개 모델을 ablation으로 최적화하며 개발"
    label_en: "Developed ~10 structure/prosthesis-segmentation and lesion-detection models, optimized via ablation"
    uses: [f1, f2, f4, f6]
  - label_ko: "병변 평가를 detection 레벨로 전환하도록 기획팀을 설득"
    label_en: "Persuaded the planning team to evaluate lesions at the detection level"
    uses: [f3]
  - label_ko: "라벨링 가속용 SAM을 파인튜닝하고, 결과를 LLM 요약 파이프라인으로 확장"
    label_en: "Fine-tuned a SAM labeling model and extended outputs into an LLM summary pipeline"
    uses: [f5, f10]
  - label_ko: "학습 모델을 C++·DLL로 패키징해 앱 개발팀에 이관"
    label_en: "Packaged trained models as C++/DLLs and handed off to the app team"
    uses: [f8]

facts:
  f1: {kind: scope, value_ko: "치과 파노라마에서 치아·하치조신경관·상악동·보철물(크라운·임플란트·인레이·브릿지)·근관치료 분할과 우식증·치주염·매복치·잔존치근 탐지 등 10여 개 모델을 개발", value_en: "developed ~10 models on dental panoramic images — segmentation of teeth, inferior alveolar nerve canal, maxillary sinus, prosthetics (crown, implant, inlay, bridge) and root-canal treatment, plus detection of caries, periodontitis, impacted teeth, and residual roots", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "분할은 Mask2Former·MaskDINO(트랜스포머)와 U-Net(전통)으로, 검출은 YOLO·Detectron2·MMDetection 등 다양한 프레임워크로 모델을 개발", value_en: "built segmentation models on transformer backbones (Mask2Former, MaskDINO) and a traditional U-Net, and detection models across frameworks such as YOLO, Detectron2, and MMDetection", disclosure: public, confidence: measured}
  f3: {kind: decision, value_ko: "병변을 마스크로 정의하는 것의 모순을 근거로 기획팀을 설득해, 병변 평가를 detection 레벨로 전환", value_en: "persuaded the planning team, with evidence, to evaluate lesions at the detection level instead of forcing mask-based ground truth", disclosure: public, confidence: measured}
  f4: {kind: decision, value_ko: "모델 구분과 task 통합을 다수의 ablation 실험으로 비교해 최적 구성을 도출", value_en: "compared many model splits and task groupings through numerous ablation experiments to arrive at the optimal configuration", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "라벨링 툴용 SAM 모델을 자사 데이터·dental panorama로 파인튜닝해 치아 마스크 라벨링 시간·비용을 절감", value_en: "fine-tuned a SAM model for the labeling tool on in-house data and dental panoramas to cut teeth-mask labeling time and cost", disclosure: public, confidence: measured}
  f6: {kind: scope, value_ko: "벤치마킹 대상 타사 제품의 제공 항목 범위를 전부 커버", value_en: "covered the full range of items offered by the benchmarked competitor product", disclosure: public, confidence: measured}
  f7: {kind: metric, value_ko: "분할·검출 정량 지표를 확보 (사내 비공개)", value_en: "quantitative segmentation/detection metrics (internal)", disclosure: internal, confidence: measured}
  f8: {kind: artifact, value_ko: "학습 모델을 C++로 변환하고 DLL로 패키징해 애플리케이션 개발팀에 이관", value_en: "converted the trained models to C++ and packaged them as DLLs, handed off to the application development team", disclosure: public, confidence: measured}
  f9: {kind: decision, value_ko: "제품 기획, 목표 수준 설정, 학습 데이터 구축부터 제품화까지 파노라마 모델 개발을 scratch에서 end-to-end로 리드", value_en: "led panoramic model development end to end from product planning, target-setting, and dataset construction through productization", disclosure: public, confidence: measured}
  f10: {kind: artifact, value_ko: "파노라마 모델 결과로 LLM 요약 설명을 생성하는 파이프라인을 개발 (로컬 모델을 다양하게 테스트한 후 목적에 맞는 모델·프롬프트로 구성)", value_en: "built a pipeline that uses the panoramic model outputs to generate summary explanations with an LLM (after testing various local models, settled on a fit-for-purpose model and prompt)", disclosure: public, confidence: measured}
  # 학습 데이터 구축·운영은 p12 참조 (SAM 라벨링 모델 포함)

variants:
  - angle: ownership-e2e
    uses: [f9]
    ko: "제품 기획, 목표 수준 설정, 학습 데이터 구축부터 제품화까지 치과 파노라마 모델 개발을 scratch에서 end-to-end로 리드"
    en: "Led dental-panoramic model development end to end — from product planning, target-setting, and dataset construction through productization"
  - angle: modeling-foundation
    uses: [f1]
    ko: "치과 파노라마에서 해부 구조·보철물 분할과 병변 탐지를 아우르는 10여 개 모델을 설계·학습"
    en: "Designed and trained ~10 models spanning anatomical-structure and prosthesis segmentation and lesion detection on dental panoramic images"
  - angle: modeling-foundation
    uses: [f2, f4]
    ko: "Mask2Former·MaskDINO(트랜스포머)와 U-Net(전통) 모델을 다수의 ablation 실험으로 비교해 최적 구성을 도출"
    en: "Compared transformer models (Mask2Former, MaskDINO) and a traditional U-Net through many ablation experiments to arrive at the optimal configuration"
  - angle: stakeholder-alignment
    uses: [f3]
    ko: "병변을 마스크로 정의하는 것의 모순을 근거로 기획팀을 설득해, 병변 평가를 detection 레벨로 전환"
    en: "Persuaded the planning team, with evidence, to evaluate lesions at the detection level instead of forcing mask-based ground truth"

short:
  ko: >
    치과 파노라마에서 치아·신경관·상악동·보철물 분할과 우식증·치주염·매복치·잔존치근 탐지 등
    10여 개 모델을 scratch에서 end-to-end로 리드. 분할은 Mask2Former·MaskDINO(트랜스포머)와
    U-Net(전통)을 다수의 ablation으로 비교하고, 라벨링 툴용 SAM을 파인튜닝해 라벨링 비용을 절감.
    병변은 마스크 정답의 모순을 근거로 기획팀을 설득해 detection 평가로 전환. 벤치마킹 대상
    타사 제품의 제공 범위를 전부 커버.
  en: >
    Led ~10 models end to end on dental panoramic images — segmentation of teeth, nerve canal,
    sinus, and prosthetics plus detection of caries, periodontitis, impacted teeth, and residual
    roots. Compared transformer (Mask2Former, MaskDINO) and traditional (U-Net) models via many
    ablations, and fine-tuned a SAM labeling model to cut labeling cost. Persuaded the planning
    team to evaluate lesions at the detection level, and covered the full range of the benchmarked
    competitor product.
---

## 1. 문제 정의와 제약조건
- 치과 파노라마에서 다종 해부 구조·보철물·병변을 자동 인식 (요구사항이 많고 복잡)
- 병변은 특성상 '정확한' 마스크 정답 자체에 모순이 존재
- 제품 기획·목표 수준 정의부터 학습 데이터까지 처음부터 정립

## 2. 접근과 대안 비교
- **병변 평가 방식**: 기획팀은 병변도 segmentation(마스크)로 요청 → 정밀 마스크 정답 생성의
  모순을 근거로 설득해 **detection 레벨 평가**로 전환
- **모델 아키텍처**: 분할은 Mask2Former·MaskDINO(트랜스포머)와 U-Net(전통)을 테스트하고, 검출은
  YOLO·Detectron2·MMDetection 등 다양한 프레임워크를 활용. 모델 구분과 task 통합을 바꿔가며
  **다수의 ablation 실험**으로 최적 구성을 도출

## 3. 구현
- 분할: Mask2Former·MaskDINO·U-Net 기반
- **라벨링 가속**: 라벨링 툴에 넣을 SAM 모델을 자사 데이터 + dental panorama로 파인튜닝 → 치아
  마스크 라벨링 시간·비용을 절감 (학습 데이터 구축 상세는 **p12** 참조)
- **LLM 요약**: 파노라마 모델 결과로 LLM 요약 설명을 생성하는 파이프라인을 간단히
  개발 (로컬 모델을 다양하게 테스트한 후 목적에 맞는 모델·프롬프트를 선정)

## 4. 검증
- 정량 지표는 **사내 비공개**
- 임상 자문의 평가 기준으로 품질을 확인
- 벤치마킹 대상 타사 제품의 제공 항목 범위를 전부 커버

## 5. 결과
- 정밀한 마스크 수준으로 구현
- 타사 제품의 제공 범위를 전부 커버, 임상 자문의 평가상 정밀도는 동등하거나 더 나은 수준
  (정량 지표 비공개)

## 6. 난이도 · 한계
- 요구사항이 많고 제품 기획·목표 수준·데이터까지 scratch에서 정의 — 가장 난이도가 높았던 프로젝트
