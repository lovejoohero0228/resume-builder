---
id: p11
title_ko: "C-arm Auto Positioning 리서치"
title_en: "C-arm Auto Positioning Research"
org: "Genoray"
period: "2026-06 ~ 진행중"
role: "리드"
role_note_ko: "팀원 1명과 협업"
role_note_en: "With one teammate"
tags: ["Medical AI", "Multimodal", "Vision", "Research"]
angles: [research-depth, ownership-e2e]

problem:
  goal_ko: "1회 촬영만으로 타겟 구조물을 정확한 포지션으로 정렬 시키기 위해 각 축별 이동·회전 delta 값을 추론하는 Auto Positioning 모델 연구"
  goal_en: "Research an Auto Positioning model that infers per-axis translation/rotation deltas to align a target structure in a single shot."
  hurdle_ko: |
    - 전문가(의사 / 방사선사)의 임상 경험으로 만들어진 암묵지 데이터 확보 필요
  hurdle_en: |
    - Requires tacit-knowledge data formed from the clinical experience of experts (doctors / radiographers)

role_groups:
  - label_ko: "학습 데이터 구축을 위한 두 전략을 병렬로 진행, 합성 데이터 활용 연구 & 실 데이터 확보"
    label_en: "Ran two data strategies in parallel — synthetic-data research and real-data acquisition"
    uses: [f1, f2]
  - label_ko: "C-arm Auto Positioning 선행 연구 재현을 통한 모델링 기획"
    label_en: "Planned modeling by reproducing prior work on C-arm Auto Positioning"
    uses: [f3, f4]

facts:
  f1: {kind: artifact, value_ko: "실데이터 확보 지연 문제를 CT 기반 DeepDRR 선행연구 재현으로 보완 — CT 영상에서 projection 영상을 생성하는 연구", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "임상 데이터 혹은 phantom 데이터를 확보하기 위한 데이터 구축 프로세스 기획", value_en: "Planned a data-construction process to acquire clinical or phantom data", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "3D C-arm 장비에서 최초의 촬영 영상 한 장만으로, 목표 위치까지의 축 별 이동량을 학습하는 선행 연구 논문 조사 및 구현", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "입력: 스카우트 촬영 영상 → 출력: 축별 이동 delta 값", value_en: "", disclosure: public, confidence: measured}

variants:
  - angle: research-depth
    uses: [f3, f1]
    ko: "단일 스카우트 촬영만으로 축별 이동 delta를 추론하는 C-arm Auto Positioning 선행 연구를 조사·재현하고, 실데이터 확보 지연을 CT 기반 DeepDRR 합성 영상 생성으로 보완"
    en: "Surveyed and reproduced prior work on C-arm Auto Positioning that infers per-axis translation deltas from a single scout shot, and mitigated real-data delays with CT-based DeepDRR synthetic projections"
  - angle: ownership-e2e
    uses: [f1, f2]
    ko: "합성 데이터 연구와 실데이터 확보 두 전략을 병렬로 진행하며 임상·phantom 데이터 구축 프로세스를 기획"
    en: "Ran synthetic-data research and real-data acquisition in parallel, planning a clinical/phantom data-construction process"

short:
  ko: "단일 스카우트 촬영만으로 축별 이동 delta를 추론하는 C-arm Auto Positioning 선행 연구를 조사·재현하고, 실데이터 확보 지연을 CT 기반 DeepDRR 합성 영상 생성으로 보완"
  en: "Surveyed and reproduced prior work on C-arm Auto Positioning that infers per-axis translation deltas from a single scout shot, and mitigated real-data delays with CT-based DeepDRR synthetic projections"
---
