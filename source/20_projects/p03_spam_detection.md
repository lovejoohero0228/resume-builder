---
id: p03
title_ko: "BERT 기반 스팸 게시글 탐지 개발"
title_en: "BERT-based Spam Post Detection"
org: "Blind"
period: "2022-12 ~ 2024-02"
role: "참여"
role_note_ko: "팀장 1명과 협업"
role_note_en: "With one team lead"
tags: ["B2C Platform", "LLM", "Classification"]
angles: [ownership-e2e, engineering-craft]

problem:
  goal_ko: "직장인 커뮤니티 'Blind ’에서 컨텐츠 QA팀의 업무를 부분 자동화하기 위해 스팸 게시글을 자동으로 걸러내는 탐지 모델 구축"
  goal_en: "Build a detection model that auto-filters spam posts to partly automate the content-QA team's work at the professional community 'Blind'."
  hurdle_ko: |
    - 스팸과 정상 데이터의 샘플 수 불균형 문제
    - 학습 데이터로 활용된 내부 컨텐츠 QA 로그 데이터의 정제 난이도
  hurdle_en: |
    - Class imbalance between spam and normal samples
    - Difficulty cleaning the internal content-QA log data used for training

role_groups:
  - label_ko: "BERT 기반 스팸 게시글 분류 모델을 fine-tuning"
    label_en: "Fine-tuned a BERT-based spam-post classification model"
    uses: [f1, f2]
  - label_ko: "SQL 추출부터 학습·배포·모니터링까지 파이프라인 전체를 소유"
    label_en: "Owned the whole pipeline from SQL extraction through training, deployment, and monitoring"
    uses: [f3, f4]

facts:
  f1: {kind: artifact, value_ko: "AWS 환경에서 BERT 모델을 fine-tuning하는 방식으로 스팸  분류 모델 학습", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "LLM 기반 데이터 증강으로 학습 데이터를 보강하여 클래스 불균형 문제 돌파", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "내부 컨텐츠 QA 로그를 SQL로 추출하여 학습에 활용 가능한 형태로 정제하는 파이프라인 개발", value_en: "Built a pipeline that extracts internal content-QA logs via SQL and cleans them into a trainable form", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "서비스 배포 후, Apache Superset 대시보드로 성능 모니터링", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: metric, value_ko: "내부 컨텐츠 QA팀이 직접 검수하던 스팸 물량 중 35%를 자동 플래그 처리하여 업무 효율 개선", value_en: "Auto-flagged 35% of the spam volume the internal content-QA team had reviewed by hand, improving their workflow", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1, f3, f4, f5]
    ko: "AWS에서 BERT 스팸 분류 모델을 파인튜닝하고 SQL 추출→학습→배포→모니터링(Apache Superset) 파이프라인을 소유, 인간 검수 전 스팸의 35%를 자동 플래그"
    en: "Fine-tuned a BERT spam classifier on AWS and owned the SQL-extraction to training to deployment to monitoring (Apache Superset) pipeline, auto-flagging 35% of spam before human review"
  - angle: engineering-craft
    uses: [f2, f3]
    ko: "LLM 기반 데이터 증강으로 클래스 불균형을 완화하고 내부 컨텐츠 QA 로그를 SQL로 정제하는 학습 파이프라인을 구축"
    en: "Mitigated class imbalance with LLM-based data augmentation and built a training pipeline that cleans internal content-QA logs extracted via SQL"

short:
  ko: "AWS에서 BERT 스팸 분류 모델을 파인튜닝하고 SQL 추출→학습→배포→모니터링(Apache Superset) 파이프라인을 소유, 인간 검수 전 스팸의 35%를 자동 플래그"
  en: "Fine-tuned a BERT spam classifier on AWS and owned the SQL-extraction to training to deployment to monitoring (Apache Superset) pipeline, auto-flagging 35% of spam before human review"
---
