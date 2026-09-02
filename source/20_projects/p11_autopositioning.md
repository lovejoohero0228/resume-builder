---
id: p11
title_ko: C-arm Auto Positioning 리서치
title_en: C-arm Auto Positioning Research
org: Genoray
period: 2026-06 ~ 진행중
role: "리드 (2인 팀; 신입이 메인, 서포트에서 리딩으로)"
tags: [Medical-AI, Vision, Multimodal]
angles: [research-depth, engineering-craft, ownership-e2e]

card:
  ko: "임상 데이터가 부족한 상황에서 합성 데이터로 C-arm 자동 자세 추론 모델을 연구 (진행 중)"
  en: "Researching C-arm Auto Positioning with synthetic data amid data scarcity (ongoing)"

problem:
  goal_ko: "scout 영상에서 타겟 구조물을 정답 포지션으로 정렬시킬 각 축별 이동·회전 delta를 추론하는 Auto Positioning 모델 연구."
  goal_en: "Research an Auto Positioning model that, from a scout image, infers the per-axis translation/rotation deltas needed to align the target structure into the correct pose."
  hurdle_ko: |
    - 실제 방사선 촬영 임상 데이터 확보가 협의 대기 중 (데이터 부족)
    - 리서치·모델링 기획 단계 — 성능 검증 아직 불가
  hurdle_en: |
    - Access to real radiographic clinical data is pending agreements (data scarcity)
    - Still at the research / modeling-planning stage, so performance validation isn't yet possible

role_groups:
  - label_ko: "scout 영상을 기반으로 축별 delta를 추론하는 Auto Positioning 모델을 연구"
    label_en: "Researched the scout-image, per-axis-delta Auto Positioning model"
    uses: [f1]
  - label_ko: "실데이터 확보 지연을 CT 기반 DeepDRR 선행연구 재현으로 보완"
    label_en: "Offset delayed real data by reproducing CT-based DeepDRR prior work"
    uses: [f2]
  - label_ko: "합성 데이터 보완과 팬텀 실촬영, 두 데이터 전략을 병렬로 기획"
    label_en: "Planned two data strategies in parallel — synthetic augmentation vs. phantom capture"
    uses: [f3]

facts:
  f1: {kind: artifact, value_ko: "scout 영상에서 타겟 구조물을 정답 포지션으로 정렬시킬 각 축별 이동·회전 delta를 추론하는 모델 연구", value_en: "researching a model that infers per-axis translation/rotation deltas — from a scout image — to move/rotate the device so the target structure appears in the correctly aligned pose", disclosure: public, confidence: measured}
  f2: {kind: decision, value_ko: "실 임상 데이터 획득이 협의 대기 중이라, CT에서 C-arm 유사 projection 영상을 생성하는 DeepDRR 선행연구를 재현·테스트", value_en: "with access to real clinical data delayed by pending agreements, reproduced and tested DeepDRR prior work that generates C-arm-like projection images from CT volumes", disclosure: public, confidence: measured}
  f3: {kind: decision, value_ko: "합성 데이터의 한계 보완과 팬텀 실촬영 데이터 획득, 두 방향의 기획을 병렬로 진행", value_en: "planning two data strategies in parallel — augmenting around synthetic-data limits, or acquiring real data via a phantom", disclosure: public, confidence: measured}
  # 성능 검증 미진행 (리서치·모델링 기획 단계) / 디지털 트윈은 p01 참조

variants:
  - angle: research-depth
    uses: [f1, f2]
    ko: "scout 영상에서 각 축별 이동·회전 delta를 추론하는 Auto Positioning 모델을 연구하고, 실데이터 확보 지연을 CT 기반 DeepDRR 선행연구 재현으로 보완"
    en: "Researched an Auto Positioning model that infers per-axis translation/rotation deltas from a scout image, offsetting delayed real data by reproducing CT-based DeepDRR prior work"
  - angle: engineering-craft
    uses: [f2]
    ko: "CT 영상에서 C-arm projection 유사 영상을 생성하는 DeepDRR 파이프라인을 재현·구성"
    en: "Reproduced and set up a DeepDRR pipeline that generates C-arm-like projection images from CT volumes"
  - angle: ownership-e2e
    uses: [f3]
    ko: "실데이터 획득이 지연되는 가운데 합성 데이터 보완과 팬텀 실촬영, 두 방향의 데이터 전략·기획을 병렬로 주도"
    en: "Drove two parallel data strategies — synthetic-data augmentation and phantom-based real capture — amid delayed real-data access"

short:
  ko: >
    scout 영상에서 타겟 구조물을 정답 포지션으로 정렬시킬 각 축별 이동·회전 delta를 추론하는
    Auto Positioning 모델을 리서치. 실 임상 데이터 획득 지연을 CT 기반 DeepDRR 선행연구 재현으로 보완하고,
    합성 데이터 보완과 팬텀 실촬영, 두 방향의 데이터 전략을 병렬로 기획 중. (리서치·모델링 기획 단계,
    진행중)
  en: >
    Research on an Auto Positioning model that infers per-axis deltas from a scout image to move/
    rotate the device so the target structure lands in the aligned pose. Offsetting delayed clinical
    data by reproducing CT-based DeepDRR prior work, and planning two data strategies in parallel —
    synthetic augmentation and phantom capture. (Research / modeling-planning stage, ongoing.)
---

## 1. 문제 정의와 제약조건
- scout 영상에서 타겟 구조물을 정답 포지션으로 정렬시킬 각 축별 이동·회전 delta를 추론
- 제약: 실 방사선 촬영 임상 데이터 획득이 협의 대기 중 (데이터 부족)

## 2. 접근과 대안 비교
- **합성 데이터**: CT에서 C-arm projection 유사 영상을 생성하는 DeepDRR 선행연구를 재현·테스트
- **데이터 전략(병렬 기획)**: 합성 데이터의 한계 보완과 팬텀 실촬영, 방향별 기획을 병렬로 진행

## 3. 구현
- (리서치·모델링 기획 단계) DeepDRR 파이프라인을 재현
- 디지털 트윈 테스트 환경은 **p01** 참조

## 4. 검증
- 성능 검증 미진행 (진행중)

## 5. 결과
- 진행중

## 6. 한계와 다음 단계
- 진행중 — 데이터 확보 방향 확정 후 성능 검증 예정
