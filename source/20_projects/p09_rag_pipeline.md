---
id: p09
title_ko: "규정·조례 문서 RAG 챗봇 개발 — 서울시여성가족재단"
title_en: "Regulation/Ordinance Document RAG Chatbot — Seoul Foundation of Women & Family"
org: "Dfinite"
period: "2024-10 ~ 2024-12"
role: "리드"
role_note_ko: "서울시여성가족재단 PoC 개발 End-to-end 담당"
role_note_en: "Owned the Seoul Foundation PoC end to end"
tags: ["RAG", "LLM"]
angles: [engineering-craft, performance-optimization, stakeholder-alignment]

problem:
  goal_ko: "규정·행정 · 문의 등을 내부 문서 근거로 정확히 응답하는 RAG 챗봇 구축"
  goal_en: "Build a RAG chatbot that answers regulation/administrative questions accurately, grounded in internal documents."
  hurdle_ko: |
    - 준법률 성격(규정·조례)이라 환각 제어가 핵심 — 문서에 없는 틀린 답을 주는 것이 치명적
    - 다양한 원문 형식 —  HWP·Word·PDF·Excel 등 (이미지로 첨부된 표 포함)
    - 부서·직급별 접근 권한 분리 요청
  hurdle_en: |
    - Quasi-legal content (rules/ordinances) makes hallucination control critical — a wrong answer not in the docs is costly
    - Many source formats — HWP, Word, PDF, Excel (including tables attached as images)
    - Access separated by department and rank was requested

role_groups:
  - label_ko: "내부 문서 60여 개를 기반으로 RAG 챗봇 PoC를 단독 개발"
    label_en: "Solo-built a RAG chatbot PoC over 60+ internal documents"
    uses: [f1]
  - label_ko: "텍스트 추출·파싱·임베딩, Retrieval, 답변 생성으로 이어지는 파이프라인을 구축"
    label_en: "Built the extract/parse/embed → retrieval → answer-generation pipeline"
    uses: [f2, f3, f4]
  - label_ko: "준법률 도메인의 환각을 억제하기 위해 출처 명시·검증 단계를 설계"
    label_en: "Designed source citation and a verification step to suppress hallucination in a quasi-legal domain"
    uses: [f5]
  - label_ko: "부서·직급별 접근 권한 분리를 구현"
    label_en: "Implemented access control separated by department and rank"
    uses: [f6]
  - label_ko: "고객사와 함께 로그 분석·피드백으로 지속 개선"
    label_en: "Kept improving via client log analysis and feedback"
    uses: [f7]

facts:
  f1: {kind: artifact, value_ko: "서울시여성가족재단의 내부 규정집·조례·예산 등 60여 개 문서를 기반으로 RAG 문서 챗봇을 단독 개발 (LangChain + 직접 구현)", value_en: "", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "HWP·Word·PDF·Excel·이미지 파일 등 다양한 형식에서 정보를 왜곡 없이 hierarchy 대로 추출·파싱", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "최적의 의미 단위로 청킹하고 임베딩 모델을 활용하여 벡터DB에 임베딩, 요약 등의 방식으로 메타데이터 생성", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "BM25와 같은 랭킹 알고리즘 설계, retrieve한 정보를 활용하여 자연스러운 답변 생성", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "준법률 도메인이라 환각 제어가 핵심 — 프롬프트 억제와 검증 단계를 추가하고, 모든 답변에 출처(문서명·관련성 점수)를 명시", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "부서별·직급별 접근 권한을 차별화하는 관리 기능을 구현", value_en: "Implemented differentiated access control by department and rank", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "고객사와 긴밀히 소통하며 로그 분석·피드백 반영으로 개선", value_en: "", disclosure: public, confidence: measured}
  f8: {kind: metric, value_ko: "파일 검색 성능 96%·청크 검색 성능 88% 달성", value_en: "Achieved 96% file-retrieval and 88% chunk-retrieval performance", disclosure: public, confidence: measured}

variants:
  - angle: engineering-craft
    uses: [f1, f2, f4]
    ko: "규정·조례 등 내부 문서 60여 개 기반 RAG 챗봇을 단독 구축 — 다형식(HWP·Word·PDF·Excel) 추출·파싱·청킹·임베딩부터 BM25 하이브리드 검색·답변 생성까지 (LangChain+직접 구현)"
    en: "Solo-built a RAG chatbot over 60+ internal documents (rules, ordinances) — from multi-format (HWP/Word/PDF/Excel) extraction, parsing, chunking, and embedding to BM25 hybrid retrieval and answer generation (LangChain plus custom code)"
  - angle: performance-optimization
    uses: [f8]
    ko: "파일 검색 성능 96%·청크 검색 성능 88%를 달성"
    en: "Achieved 96% file-retrieval and 88% chunk-retrieval performance"
  - angle: stakeholder-alignment
    uses: [f5, f6, f7]
    ko: "준법률 도메인의 환각을 억제하기 위해 출처 명시·검증 단계를 설계하고, 부서·직급별 접근 권한 분리와 고객사 로그 분석·피드백으로 지속 개선"
    en: "Suppressed hallucination in a quasi-legal domain via source citation and a verification step, and kept improving with department/rank access control and client log analysis"

short:
  ko: "규정·조례 등 내부 문서 60여 개 기반 RAG 챗봇을 단독 구축 — 다형식(HWP·Word·PDF·Excel) 추출·파싱·청킹·임베딩부터 BM25 하이브리드 검색·답변 생성까지 (LangChain+직접 구현)"
  en: "Solo-built a RAG chatbot over 60+ internal documents (rules, ordinances) — from multi-format (HWP/Word/PDF/Excel) extraction, parsing, chunking, and embedding to BM25 hybrid retrieval and answer generation (LangChain plus custom code)"
---
