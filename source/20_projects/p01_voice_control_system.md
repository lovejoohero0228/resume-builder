---
id: p01
title_ko: C-arm 음성 제어 시스템
title_en: C-arm AI Voice System
org: Genoray
period: 2026-01 ~ 2026-11
role: "리드 (임상 요구조사~구현 — 신입 팀원 1명과 협업 / 배포·엔지니어링 — 단독)"
tags: [Medical-AI, Speech, NLP, On-device]
angles: [ownership-e2e, performance-optimization, engineering-craft]

card:
  ko: "손댈 수 없는 수술 환경을 위해, 지연·온디바이스 제약을 뚫고 C-arm 음성 제어를 설계·배포"
  en: "Owned the C-arm AI Voice System under real-time, on-device constraints"

problem:
  goal_ko: "수술 중 멸균 상태에서도 손대지 않고 C-arm을 조작하도록, 음성 명령 기반 비접촉 제어를 자사 장비에 내재화"
  goal_en: "Bring hands-free, voice-based control into our own C-arm so surgeons can operate it while sterile — without touching the device."
  hurdle_ko: |
    - 수술 중 실시간으로 쓰이는 만큼 응답 지연이 가장 치명적
    - 온디바이스 동작 필수, 의료 도메인 네트워크 보안(외부 연결 제한)
    - 한국어·의료 특수 용어의 음성 인식이 까다로움
  hurdle_en: |
    - Latency is the most critical constraint (real-time use in surgery)
    - Must run on-device; medical-domain network security limits external connectivity
    - Hard Korean / domain-specific medical-term speech recognition

role_groups:
  - label_ko: "음성 명령을 장비 동작으로 바꾸는 파이프라인을 설계·구현"
    label_en: "Designed and built the Voice-to-Command pipeline (voice → device motion)"
    uses: [f3, f5, f17]
  - label_ko: "STT 응답 지연·오인식을 최적화"
    label_en: "Optimized STT latency and misrecognition"
    uses: [f8, f18]
  - label_ko: "제약에 맞춰 아키텍처를 전환·확정하고 예외 처리를 설계"
    label_en: "Pivoted and locked the architecture to fit constraints; designed exception handling"
    uses: [f12, f13, f14, f15]
  - label_ko: "물리 장비 없이 개발·검증할 3D-CAD 디지털 트윈 환경을 구축"
    label_en: "Built a 3D-CAD digital-twin environment to develop/validate without the device"
    uses: [f16]
  - label_ko: "온디바이스 배포·패키징·유지보수 체계를 단독 구축"
    label_en: "Solo-built on-device deployment, packaging, and maintenance"
    uses: [f9, f10, f11]

facts:
  # --- 음성 → NLU → 모터 제어 파이프라인 ---
  f1: {kind: metric, value_ko: "STT·NLU 전체 콜 정확도 86% → 94%", value_en: "full-call (STT·NLU) accuracy 86% → 94%", disclosure: public, confidence: measured}
  f2: {kind: metric, value_ko: "음성 명령 인식 정확도 96%", value_en: "96% command accuracy", disclosure: public, confidence: measured}
  f3: {kind: artifact, value_ko: "한국어 음성 → NLU → 모터 제어 파이프라인으로 C-arm 수술 장비를 구동", value_en: "Korean voice → NLU → motor-control pipeline driving a C-arm surgical device", disclosure: public, confidence: measured}
  f5: {kind: artifact, value_ko: "자모 분해 유사도 기반 fallback 매칭 단계", value_en: "Jamo-decomposition similarity fallback matching stage", disclosure: public, confidence: measured}
  f6: {kind: adoption, value_ko: "물리 디바이스에서 검증했고, 출시 전 규제 인증을 진행 중", value_en: "validated on the device, in regulatory certification prior to release", disclosure: public, confidence: recalled}
  # --- STT 지연 최적화 (구 p04) ---
  f7: {kind: metric, value_ko: "STT 응답 지연 4초 초과 → 0.4초 미만", value_en: "STT latency 4s+ → under 0.4s", disclosure: public, confidence: measured}
  f8: {kind: decision, value_ko: "Faster Whisper를 채택하고 FFmpeg 전처리 병목을 규명", value_en: "adopted Faster Whisper and identified an FFmpeg preprocessing bottleneck", disclosure: public, confidence: measured}
  # --- 배포 / 엔지니어링 (단독) ---
  f9: {kind: decision, value_ko: "Python 전용 의존성(Faster Whisper 등) 유지하며 Nuitka로 C 변환·패키징, C# 메인 프로세스와 웹소켓 연동", value_en: "Compiled the Python service to C and packaged it via Nuitka — keeping Python-only dependencies like Faster Whisper while connecting to the C# main process over WebSocket", disclosure: public, confidence: measured}
  f10: {kind: decision, value_ko: "Nuitka·Cython으로 코드 난독화", value_en: "Used Nuitka and Cython for code obfuscation", disclosure: public, confidence: measured}
  f11: {kind: artifact, value_ko: "유지보수 체계 구축 — 회귀 단위 테스트, cfg 검증, 재학습 파이프라인, 패키징 파이프라인", value_en: "Built a maintenance system — regression unit tests, config validation, a retraining pipeline, and a packaging pipeline", disclosure: public, confidence: measured}
  # --- 접근·대안 및 한계 (설계 판단) ---
  f12: {kind: decision, value_ko: "초기에는 orchestration 기반 LLM 에이전트 구조를 구현·데모 검증했으나, 온디바이스 제약·의료 도메인 네트워크 보안·네트워크 지연으로 폐기", value_en: "Initially built and demo-validated an orchestration-based LLM agent architecture, but dropped it due to on-device constraints, medical-domain network security, and network latency", disclosure: public, confidence: measured}
  f13: {kind: decision, value_ko: "하네스 엔지니어링과 로컬 LLM 최적화로 제약 완화를 시도한 뒤, 룰베이스 + 유사도 기반 키워드 매칭 + sLLM fallback 하이브리드 구조를 최종 채택", value_en: "After trying harness engineering and local-LLM optimization to fit the constraints, adopted a hybrid architecture — rule-based + similarity-based keyword matching + sLLM fallback", disclosure: public, confidence: measured}
  f14: {kind: decision, value_ko: "룰베이스 구조의 유지보수·기능 추가·규칙 설계·단위 테스트 부담을 감수하고, 지연·보안·온디바이스 제약 아래 문제 해결을 우선", value_en: "Accepted the maintenance, feature-addition, rule-design, and unit-testing overhead of a rule-based architecture in order to satisfy latency, security, and on-device constraints", disclosure: public, confidence: measured}
  f15: {kind: decision, value_ko: "범위 밖·불확실 입력은 명령 종류에 따라 거부/무시하거나 사용자에게 다시 질의 (UX 고려)", value_en: "Handles out-of-scope or uncertain input by either rejecting/ignoring it or re-querying the user, chosen by command type for UX", disclosure: public, confidence: measured}
  f16: {kind: artifact, value_ko: "자사 장비 CAD 파일과 내부 소프트웨어 인터페이스로 실제 동작·연동하는 3D-CAD 디지털 트윈 시뮬레이션 환경을 구축 (물리 장비 없이 개발·검증)", value_en: "Built a 3D-CAD digital-twin simulation environment that actually operates and integrates via the device's CAD files and internal software interface, enabling development and validation without the physical device", disclosure: public, confidence: measured}
  f17: {kind: decision, value_ko: "의료 도메인 특수 용어(오비탈·라테랄·코달 등)의 STT 오인식에 대비해 자모 분해 유사도 기반 fallback을 도입", value_en: "introduced Jamo-decomposition similarity fallback to counter STT misrecognition of domain-specific medical terms (e.g., orbital, lateral, caudal)", disclosure: public, confidence: measured}
  f18: {kind: decision, value_ko: "소음 환경의 오인식을 소음 데이터 파인튜닝으로 개선", value_en: "improved misrecognition in noisy conditions by fine-tuning on noise data", disclosure: public, confidence: measured}

variants:
  - angle: ownership-e2e
    uses: [f3, f2]
    ko: "한국어 음성 명령을 실제 C-arm 장비의 물리적 동작으로 바꾸는 음성 → NLU → 모터 제어 파이프라인을 설계부터 디바이스 검증·배포까지 소유, 명령 인식 정확도 96% 달성"
    en: "Owned the C-arm AI Voice System end to end — a Korean Voice-to-Command (voice → NLU → motor-control) pipeline driving a C-arm surgical device — from design through on-device validation and deployment, reaching 96% command accuracy"
  - angle: ownership-e2e
    uses: [f12, f13]
    ko: "자유도 높은 orchestration 기반 LLM 에이전트 구조를 데모 검증한 뒤, 온디바이스·보안·지연 제약에 맞춰 룰베이스 + 유사도 키워드 매칭 + sLLM fallback 하이브리드로 전환·확정"
    en: "Validated an orchestration-based LLM agent architecture in a demo, then pivoted to and settled on a hybrid — rule-based + similarity keyword matching + sLLM fallback — to meet on-device, security, and latency constraints"
  - angle: performance-optimization
    uses: [f7, f8]
    ko: "FFmpeg 전처리 병목을 규명하고 Faster Whisper로 교체해 STT 응답 지연을 4초 초과에서 0.4초 미만으로 단축"
    en: "Cut STT latency from 4s+ to under 0.4s by identifying an FFmpeg preprocessing bottleneck and switching to Faster Whisper"
  - angle: performance-optimization
    uses: [f1, f2]
    ko: "STT·NLU 파이프라인의 전체 콜 정확도를 86%에서 94%로 끌어올리고 명령 인식 정확도 96% 달성"
    en: "Raised full-call accuracy from 86% to 94% and reached 96% command accuracy across the STT·NLU pipeline"
  - angle: engineering-craft
    uses: [f5, f17]
    ko: "의료 도메인 특수 용어의 STT 오인식에 대비해 자모 분해 유사도 기반 fallback 매칭으로 명령 복원 로직을 구현"
    en: "Built command-handling logic that recovers commands via Jamo-decomposition similarity fallback matching, countering STT misrecognition of domain-specific medical terms"
  - angle: engineering-craft
    uses: [f15]
    ko: "범위 밖·불확실 입력을 명령 종류에 따라 거부하거나 사용자에게 다시 질의하도록 처리 설계 (UX 고려)"
    en: "Designed out-of-scope and uncertain input handling to either reject or re-query the user depending on command type, for UX"
  - angle: engineering-craft
    uses: [f16]
    ko: "자사 장비 CAD와 내부 소프트웨어 인터페이스로 실제 연동·동작하는 3D-CAD 디지털 트윈을 구축해 물리 장비 없이 개발·검증"
    en: "Built a 3D-CAD digital twin that operates and integrates via the device's CAD files and internal software interface, enabling development and validation without the physical device"
  - angle: engineering-craft
    uses: [f9, f11]
    ko: "Python 전용 의존성(Faster Whisper 등) 유지하며 Nuitka로 C 변환·패키징, C# 메인 프로세스와 웹소켓 연동 — 회귀 단위 테스트·cfg 검증·재학습·패키징 파이프라인으로 유지보수 체계 구축"
    en: "Kept Python-only dependencies like Faster Whisper while integrating with the C# main process over WebSocket by compiling to C and packaging via Nuitka, and built a maintenance system — regression unit tests, config validation, retraining and packaging pipelines"

short:
  ko: >
    수술 중 멸균 상태에서 장비를 조작할 수 없는 문제를 해결 — 한국어 음성 명령을 C-arm 수술
    장비의 물리적 동작으로 바꾸는 음성 → NLU → 모터 제어 시스템을 설계·구현·배포. STT 응답 지연을
    4초 초과에서 0.4초 미만으로 단축하고, 유사도 기반 fallback 매칭으로 오인식에 대응 — 전체 콜
    정확도 86% → 94%·명령 인식 정확도 96% 달성. 물리 디바이스 검증 후 규제 인증을 진행 중.
  en: >
    Built the C-arm AI Voice System — a Korean Voice-to-Command (voice → NLU → motor-control)
    pipeline that turns spoken commands into physical C-arm motion, addressing the problem that
    surgeons cannot touch controls while sterile. Cut
    STT latency from 4s+ to under 0.4s and handled misrecognition with similarity-based fallback
    matching, reaching 86% → 94% full-call accuracy and 96% command accuracy. Validated on-device,
    now in regulatory certification.
---

## 1. 문제 정의와 제약조건
- 수술 중 술자가 멸균 상태에서 장비를 직접 조작할 수 없어 절차가 중단됨
- 제약:
  - **온디바이스** 동작 요건
  - 의료 도메인 **네트워크 보안** (외부 연결 제한)
  - 실시간 **응답 지연** (수술 중 사용, 가장 치명적 제약)
  - 한국어 음성 인식 특성

## 2. 접근과 대안 비교
초기에는 자유도 높은 대화를 소화하는 **orchestration 기반 LLM 에이전트 구조**를 구현·데모 검증.
온디바이스 제약·네트워크 보안·네트워크 지연 탓에 제약 완화 시도(하네스 엔지니어링, 로컬 LLM
최적화)를 거쳐 룰베이스 기반 하이브리드로 전환.

| 대안 | 장점 | 탈락 / 채택 사유 |
|---|---|---|
| orchestration 기반 LLM 에이전트 (초기 구현·데모 검증) | 자유도 높은 자연스러운 대화 처리 | 온디바이스 제약, 의료 네트워크 보안, **네트워크 지연**(치명적)으로 폐기 |
| 클라우드 LLM/STT | 정확도·표현력 | 지연·보안 제약 탓에 수술 환경에 부적합 |
| 제약 완화 시도 (하네스 엔지니어링·로컬 LLM 최적화) | 제약 내 LLM 활용 모색 | 지연·안정성 요건 미충족 |
| **채택: 룰베이스 + 유사도 기반 키워드 매칭 + sLLM fallback** | 지연·보안·온디바이스 제약을 충족하고, 오인식은 fallback으로 복원 | 유지보수·규칙 설계·테스트 부담은 감수 |

## 3. 구현
- 다이어그램: assets/diagrams/p01_pipeline.mmd
- 아키텍처: 룰베이스 + 유사도 기반 키워드 매칭 + sLLM fallback (하이브리드)
- 자모 분해 유사도 기반 fallback: 의료 도메인 특수 용어(오비탈·라테랄·코달 등)의 STT 오인식에 대비
- 범위 밖·불확실 입력 처리: 명령 종류에 따라 거부/무시하거나 다시 질의 (UX 고려)

### 3-1. 지연 최적화
- FFmpeg 전처리 병목 규명, Faster Whisper 채택 (4s+ → <0.4s)
- 측정: 사용자 음성 입력 종료 → 첫 피드백까지의 latency, 양산 PC와 동일 조건(GPU RTX3060 이상, 네트워크 미연결)에서 측정

### 3-1b. 디지털 트윈 테스트 환경
- 자사 장비 CAD와 내부 SW 인터페이스로 실제 동작·연동하는 3D-CAD 디지털 트윈을 구축 — 물리 장비 없이 개발·검증

### 3-2. 배포 · 엔지니어링 (단독)
- 패키징: Python 전용 의존성(faster-whisper 등)을 유지하기 위해 Nuitka로 C 변환·패키징하고 C# 메인 프로세스와 웹소켓 연동
- 난독화: Nuitka·Cython
- 유지보수: 회귀 단위 테스트, cfg 검증, 재학습 파이프라인, 패키징 파이프라인

## 4. 검증
- 평가축·채점 기준·게이팅 임계값 설계는 별도 평가 프레임워크로 분리 → **p02 (LLM·STT 평가 설계)** 참조
- 물리 디바이스 상에서 명령 실행 검증

## 5. 결과
- 전체 콜 정확도 86% → 94%, 명령 인식 정확도 96%
- STT 응답 지연 4초 초과 → 0.4초 미만
- Nuitka 기반 패키징으로 C# 메인 프로세스와 웹소켓 연동해 배포
- 물리 디바이스 검증 완료, 디지털 의료기기 규제 인증 프로세스 진행 중


## 6. 한계와 다음 단계
- **한계**: 룰베이스 구조라 유지보수·기능 추가·규칙 설계·단위 테스트 비용이 큼
  (제약 하 문제 해결의 트레이드오프)
- **완화**: 회귀 단위 테스트·cfg 검증·패키징 파이프라인으로 규칙 변경 회귀 부담을 일부 흡수
- **실패 모드**: 소음 환경에서의 오인식 → 소음 데이터 파인튜닝으로 개선
