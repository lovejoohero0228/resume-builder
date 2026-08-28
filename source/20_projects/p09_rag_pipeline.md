---
id: p09
title_ko: 규정·조례 문서 RAG 챗봇 (서울시여성가족재단)
title_en: Regulation/Ordinance Document RAG Chatbot (Seoul Foundation of Women & Family)
org: Dfinite
period: 2024-11 ~ 2025-01
role: 단독
tags: [Enterprise-AI, RAG, LLM]

angles: [engineering-craft, performance-optimization, stakeholder-alignment]

card:
  ko: "틀린 답이 치명적인 준법률 문서에서 환각을 억제한 RAG 챗봇을 단독 구축"
  en: "Solo-built a hallucination-controlled RAG chatbot for quasi-legal docs"

problem:
  goal_ko: "서울시여성가족재단의 반복 행정 문의(규정·휴가·재택 등)를 내부 문서 근거로 즉시 응답하는 RAG 챗봇 구축."
  goal_en: "Build a RAG chatbot that instantly answers the foundation's recurring administrative questions (rules, leave, remote work) grounded in its internal documents."
  hurdle_ko: |
    - 준법률 성격(규정·조례)이라 환각 제어가 핵심 — 틀린 답이 치명적
    - 원문 형식 제각각 (HWP·Word·PDF·Excel 등)
    - 부서·직급별 접근 권한 분리 필요
  hurdle_en: |
    - Quasi-legal content (rules/ordinances) makes hallucination control critical — a wrong answer is costly
    - Sources come in many formats (HWP, Word, PDF, Excel)
    - Access must be separated by department and rank

role_groups:
  - label_ko: "내부 문서 60여 개를 기반으로 RAG 챗봇을 단독 개발"
    label_en: "Solo-built a RAG chatbot over 60+ internal documents"
    uses: [f1]
  - label_ko: "추출·파싱·임베딩, 하이브리드 검색, 답변 생성으로 이어지는 파이프라인을 구축"
    label_en: "Built the extract/parse/embed + hybrid-retrieval + answer-generation pipeline"
    uses: [f2]
  - label_ko: "준법률 도메인의 환각을 억제하기 위해 출처 명시·검증 단계를 설계"
    label_en: "Designed source citation and a verification step to suppress hallucination in a quasi-legal domain"
    uses: [f3]
  - label_ko: "부서·직급별 접근 권한 분리를 구현"
    label_en: "Implemented access control separated by department and rank"
    uses: [f6]
  - label_ko: "고객사와 함께 로그 분석·피드백으로 지속 개선"
    label_en: "Kept improving via client log analysis and feedback"
    uses: [f5]

facts:
  f1: {kind: artifact, value_ko: "서울시여성가족재단의 내부 규정집·조례·예산 등 60여 개 핵심 문서를 기반으로 RAG 문서 챗봇을 단독 개발", value_en: "solo-built a RAG document chatbot for the Seoul Foundation of Women & Family, over 60+ core documents such as internal regulations, ordinances, and budgets", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "HWP·Word·PDF·Excel 등 다양한 형식에서 정보를 추출해 파싱·청킹하고 벡터DB에 임베딩, BM25 등 하이브리드 랭킹으로 검색, retrieve한 정보로 요약·답변을 생성 (LangChain + 직접 구현)", value_en: "extracted from many formats (HWP, Word, PDF, Excel), parsed/chunked, embedded into a vector DB, retrieved with a BM25 hybrid ranking, and generated summarized answers from retrieved passages (LangChain plus custom implementation)", disclosure: public, confidence: measured}
  f3: {kind: decision, value_ko: "준법률 도메인이라 환각 제어가 핵심 — 프롬프트 억제와 검증 단계를 추가하고, 모든 답변에 출처(문서명·관련성 점수)를 명시", value_en: "since the quasi-legal domain makes hallucination control critical, constrained prompts and added a verification step, and cited a source (document name, relevance score) on every answer", disclosure: public, confidence: measured}
  f4: {kind: metric, value_ko: "파일 검색 성능 96%(목표 90%)·청크 검색 성능 88%(목표 85%)를 달성", value_en: "achieved 96% file-retrieval performance (target 90%) and 88% chunk-retrieval performance (target 85%)", disclosure: public, confidence: measured}
  f5: {kind: decision, value_ko: "고객사와 긴밀히 소통하며 로그 분석·피드백 반영으로 개선", value_en: "worked closely with the client, analyzing logs and folding feedback back into improvements", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "부서별·직급별 접근 권한을 차별화하는 관리 기능을 구현", value_en: "implemented differentiated access control by department and rank", disclosure: public, confidence: measured}

variants:
  - angle: engineering-craft
    uses: [f2]
    ko: "HWP·Word·PDF·Excel 등 다양한 형식의 추출·파싱·청킹·임베딩부터 BM25 하이브리드 랭킹, 요약·답변 생성까지 이어지는 RAG 파이프라인을 LangChain·직접 구현으로 구축"
    en: "Built the RAG pipeline — extraction/parsing/chunking/embedding across HWP, Word, PDF, Excel, a BM25 hybrid ranking, and answer summarization — with LangChain plus custom implementation"
  - angle: performance-optimization
    uses: [f4]
    ko: "파일 검색 성능 96%(목표 90%)·청크 검색 성능 88%(목표 85%)를 달성"
    en: "Achieved 96% file-retrieval performance (target 90%) and 88% chunk-retrieval performance (target 85%)"
  - angle: stakeholder-alignment
    uses: [f5, f3]
    ko: "고객사와 긴밀히 소통하며 로그 분석·피드백을 반영해 개선하고, 준법률 도메인의 환각을 억제하기 위해 출처 명시·검증 단계를 추가"
    en: "Worked closely with the client — analyzing logs and folding in feedback — and suppressed hallucination in the quasi-legal domain with source citation and a verification step"

short:
  ko: >
    서울시여성가족재단의 내부 규정집·조례·예산 등 60여 개 문서를 기반으로 RAG 챗봇을 단독 개발.
    HWP·Word·PDF·Excel 등 다양한 형식의 추출·파싱·청킹·임베딩부터 BM25 하이브리드 랭킹, 요약·답변
    생성까지 LangChain·직접 구현으로 구축. 준법률 도메인이라 출처 명시·검증 단계로 환각을 억제.
    파일 검색 96%(목표 90%)·청크 검색 88%(목표 85%)를 달성.
  en: >
    Solo-built a RAG chatbot for the Seoul Foundation of Women & Family over 60+ internal
    regulation, ordinance, and budget documents. Extraction/parsing/chunking/embedding across HWP,
    Word, PDF, Excel, a BM25 hybrid ranking, and answer summarization — with LangChain plus custom
    code. Suppressed hallucination for the quasi-legal domain via source citation and a verification
    step. Achieved 96% file retrieval (target 90%) and 88% chunk retrieval (target 85%).
---

## 1. 문제 정의와 제약조건
- 서울시여성가족재단의 반복 행정 문의(규정·휴가·재택 등)를 내부 문서를 근거로 즉시 응답
- 준법률 성격(규정·조례)이라 **환각 제어**가 핵심 요건

## 2. 접근과 대안 비교
- 정통 RAG 기반 — LangChain에 파이프라인을 직접 구현
- 검색: dense 임베딩과 BM25 하이브리드 랭킹을 실험

## 3. 구현
- 다양한 형식(HWP·Word·PDF·Excel 등)에서 정보를 추출해 파싱·청킹하고 벡터 DB에 임베딩
- BM25 하이브리드 랭킹으로 검색하고, retrieve된 정보로 요약·답변을 생성
- 환각 제어: 프롬프트 억제와 검증 단계, 모든 답변에 출처(문서명·관련성 점수)를 명시
- 부서별·직급별 접근 권한을 차별화

## 4. 결과
- 파일 검색 성능 96% (목표 90%), 청크 검색 성능 88% (목표 85%)
- 고객사와 함께 로그 분석·피드백을 반영해 지속 개선

## 5. 결과 (요약)
- 파일 검색 96%(목표 90%)·청크 검색 88%(목표 85%)를 달성하고, 고객사 피드백을 반영해 지속 개선
