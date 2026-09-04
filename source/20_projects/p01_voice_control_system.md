---
id: p01
title_ko: "C-arm Voice AI System"
title_en: "C-arm Voice AI System"
org: "Genoray"
period: "2026-01 ~ 진행중"
role: "리드"
role_note_ko: "배포 · 엔지니어링 — 단독  /  임상 요구사항 정의 ~ PoC 구현 — 팀원 1명과 협업"
role_note_en: "Deployment & engineering — solo / clinical requirements to PoC — with one teammate"
tags: ["Medical AI", "Voice-to-Robotics", "LLM", "STT", "Optimization"]
angles: [ownership-e2e, performance-optimization, engineering-craft]

problem:
  goal_ko: "수술 중 멸균 상태에서도 손대지 않고 C-arm을 조작하도록, AI를 활용한 음성 인식 기능 추가"
  goal_en: "Add AI-based voice recognition so the C-arm can be operated hands-free while sterile during surgery."
  hurdle_ko: |
    - 수술 중 실시간으로 쓰이는 만큼 응답 지연이 가장 치명적
    - 온디바이스 동작 필수, 폐쇠망에서 작동해야하는 도메인 특성
    - 의학 특수 용어의 STT 음성 인식 품질
  hurdle_en: |
    - Real-time surgical use makes response latency the most critical factor
    - Must run on-device, within a closed network per the domain
    - STT recognition quality for specialized medical terminology

role_groups:
  - label_ko: "Voice-to-Command 파이프라인(음성 → 장비 동작)을 설계·구현"
    label_en: "Designed and built the Voice-to-Command pipeline (voice → device motion)"
    uses: [f1, f2]
  - label_ko: "STT 응답 지연·오인식을 최적화"
    label_en: "Optimized STT response latency and misrecognition"
    uses: [f3, f4]
  - label_ko: "제약에 맞춰 아키텍처를 전환·확정하고 예외 처리를 설계"
    label_en: "Pivoted and finalized the architecture under constraints, and designed exception handling"
    uses: [f5, f6, f7, f8]
  - label_ko: "물리 장비 없이 개발·검증할 3D-CAD 디지털 트윈 환경을 구축"
    label_en: "Built a 3D-CAD digital twin to develop and verify without physical hardware"
    uses: [f9]
  - label_ko: "온디바이스 배포·패키징·유지보수 체계를 단독 구축"
    label_en: "Solo-built the on-device deployment, packaging, and maintenance system"
    uses: [f10, f11]

facts:
  f1: {kind: artifact, value_ko: "한국어 음성 → NLU → 모터 제어 파이프라인으로 C-arm 수술 장비를 구동", value_en: "Drove the C-arm surgical device via a Korean speech to NLU to motor-control pipeline", disclosure: public, confidence: measured}
  f2: {kind: artifact, value_ko: "의료 도메인 특수 용어(오비탈·라테랄·코달 등)의 STT 오인식에 대비해 자모 분해 유사도 기반 fallback을 도입", value_en: "", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "다양한 STT 모델 비교 실험을 통해 Faster Whisper 모델 채택 및 품질 최적화", value_en: "", disclosure: public, confidence: measured}
  f4: {kind: artifact, value_ko: "소음 환경의 오인식을 소음 데이터 Fine-tuning으로 개선", value_en: "", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "초기에는 orchestration 기반 LLM 에이전트 구조를 구현했으나, 온디바이스 제약·의료 도메인 네트워크 보안·네트워크 지연으로 설계 변경", value_en: "", disclosure: public, confidence: measured}
  f6: {kind: artifact, value_ko: "하네스 엔지니어링과 로컬 LLM 최적화로 제약 완화를 시도한 뒤, 룰베이스 + 유사도 기반 검색 + sLLM fallback 하이브리드 구조를 최종 채택", value_en: "", disclosure: public, confidence: measured}
  f7: {kind: artifact, value_ko: "룰베이스 구조의 유지보수·기능 추가·규칙 설계·단위 테스트 부담을 감수하고, 지연·보안·온디바이스 제약 아래 문제 해결을 우선", value_en: "", disclosure: public, confidence: measured}
  f8: {kind: artifact, value_ko: "범위 밖·불확실 입력은 명령 종류에 따라 거부/무시하거나 사용자에게 다시 질의하는 안전 가드레일 설계", value_en: "", disclosure: public, confidence: measured}
  f9: {kind: artifact, value_ko: "자사 장비 CAD 파일과 장비 제어 SW 인터페이스로 실제 동작·연동하는 3D 디지털 트윈 시뮬레이션 개발", value_en: "", disclosure: public, confidence: measured}
  f10: {kind: artifact, value_ko: "Python 전용 의존성(Faster Whisper 등) 유지하며 Nuitka로 C 변환 · 패키징, C# 메인 프로세스와 웹소켓 연동", value_en: "", disclosure: public, confidence: measured}
  f11: {kind: artifact, value_ko: "유지보수 체계 구축 — 회귀 단위 테스트, 재학습 파이프라인, 패키징 파이프라인", value_en: "", disclosure: public, confidence: measured}
  f12: {kind: metric, value_ko: "STT·NLU End-to-End 정확도 94%", value_en: "STT·NLU end-to-end accuracy 94%", disclosure: public, confidence: measured}
  f13: {kind: metric, value_ko: "STT 응답 시간: 4초→ 0.4초 미만", value_en: "STT response time: 4s → under 0.4s", disclosure: public, confidence: measured}
  f14: {kind: adoption, value_ko: "물리 디바이스와의 연동 검증 완료, 출시 전 인증 절차 진행 중", value_en: "Physical-device integration verified; pre-launch certification in progress", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f1, f6, f8]
    ko: "수술 중 멸균 상태에서 손대지 않고 C-arm을 제어하는 음성 AI 시스템을 임상 요구 정의부터 온디바이스 배포까지 소유 — 룰베이스·유사도 검색·sLLM fallback 하이브리드로 지연·보안 제약을 해결"
    en: "Owned an on-device voice-AI system to control the C-arm hands-free during sterile surgery, from clinical requirements to deployment — resolving latency and security constraints with a rule-based + similarity-search + sLLM-fallback hybrid"
  - angle: performance-optimization
    uses: [f12, f13, f3]
    ko: "STT·NLU end-to-end 정확도 94%, STT 응답 시간 4초→0.4초 미만으로 개선 (Faster Whisper 채택·소음 데이터 파인튜닝)"
    en: "STT·NLU end-to-end accuracy 94% and STT latency improved from 4s to under 0.4s (adopted Faster Whisper, fine-tuned on noise data)"
  - angle: engineering-craft
    uses: [f1, f9, f10]
    ko: "한국어 음성→NLU→모터 제어 파이프라인과 3D-CAD 디지털 트윈을 구축하고, Python 의존성을 Nuitka로 패키징해 C# 메인 프로세스와 웹소켓 연동한 온디바이스 배포·유지보수 체계를 단독 구축"
    en: "Built the Korean speech to NLU to motor-control pipeline and a 3D-CAD digital twin, and solo-built the on-device deployment/maintenance system — Python deps packaged via Nuitka, WebSocket-linked to a C# main process"

short:
  ko: "수술 중 멸균 상태에서 손대지 않고 C-arm을 제어하는 음성 AI 시스템을 임상 요구 정의부터 온디바이스 배포까지 소유 — 룰베이스·유사도 검색·sLLM fallback 하이브리드로 지연·보안 제약을 해결"
  en: "Owned an on-device voice-AI system to control the C-arm hands-free during sterile surgery, from clinical requirements to deployment — resolving latency and security constraints with a rule-based + similarity-search + sLLM-fallback hybrid"
---
