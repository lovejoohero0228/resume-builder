# career-master

공고별 이력서·포트폴리오 버전을 조립해내는 **소스 저장소**.
완성된 문서 1개가 아니라, 검증된 사실(fact)로부터 공고에 맞는 문서를 매번 재조립한다.

## 역할 3분할

- **룰베이스** (`build.py` / `validate.py`) — 조립과 검증
- **LLM** (`assist.py`, Phase 4에서 추가) — 문장 생성과 진단
- **사람** — 사실 확정과 최종 채택

## 핵심 원칙

1. 없는 내용을 지어내지 않는다. 부족하면 `TODO:` / `[확인필요]` 마커.
2. 과장 금지. 기여 범위 동사(참여/주도/단독)를 격상하지 않는다.
3. 사실과 서술의 분리. 검증된 fact는 한 곳에만 존재하고, 모든 문장(variant)은 그 fact를 참조한다.
4. LLM은 fact를 만들지 못한다. Fact Ledger는 사람만 쓴다.
5. `disclosure: internal` fact는 공개 산출물에 절대 포함되지 않는다.

## 2층 구조

- **Fact Ledger** (불변층): 프로젝트별 원자 사실. 형용사 없음, 판단 없음, id 부여.
  - `kind`: metric | scope | artifact | decision | adoption
  - `confidence`: measured | estimated | recalled
  - `disclosure`: public | internal | range_only
- **Narrative Variants** (가변층): 같은 fact를 어떤 angle로 서술할지. 프로젝트당 최대 3 angle.

## 프로젝트 표준 형식 (필수 · 모든 프로젝트 통일)

포트폴리오 카드는 **문제 정의 → 나의 역할 → 주요 성과** 3부로 통일한다. 새 프로젝트는
`source/20_projects/_TEMPLATE.md` 를 복사해 작성하고, 아래 두 블록을 **반드시** 포함한다
(누락 시 `validate.py` 가 빌드를 막는다).

- **`problem`** — 문제 정의 2분할
  - `goal_ko` / `goal_en`: 풀고자 한 문제 (예: 외부 솔루션 내재화, 경쟁 우위 기능 탑재)
  - `hurdle_ko` / `hurdle_en`: 알려진 제약·난점 (여러 개면 `-` 불렛)
- **`role_groups`** — 나의 역할. 한 일들을 위계로 묶는다.
  - 상위 불렛 라벨은 **딱 그 문장만 읽어도 뭘 했는지 아는 짧은 액션 문장** (`label_ko`/`label_en`)
  - `uses: [fN, ...]` 로 근거 fact 연결 → 하위 불렛으로 렌더
  - metric·adoption fact 는 자동으로 **주요 성과**로 분리된다 (나의 역할엔 artifact·scope·decision만)
- 카드 상단 역할 태그(리드/주도/단독/참여)는 frontmatter `role` 문자열에서 자동 도출된다.

## 폴더 구조

```
career-master/
├── vocab.yaml              # angle / tag / 금지어 고정 어휘
├── profiles/              # 공고별 프로필 (빌드 입력)
├── source/               # 사실·서술 소스
│   ├── 00_identity.md
│   ├── 01_skills.md
│   ├── 02_education.md
│   ├── 10_experience/    # 경력 (프로젝트를 참조만)
│   ├── 20_projects/      # 프로젝트 (fact + variant)
│   ├── 30_methodology/   # 방법론 챕터
│   └── 90_appendix.md
├── assets/diagrams/      # .mmd 소스 + 렌더 결과
├── build/
│   ├── build.py          # 조립 + 검증 (룰베이스) · assemble()/catalog() (GUI용)
│   └── validate.py       # 검증기
├── app/                  # 웹 GUI (편집·조립·Export)
│   ├── server.py         # 로컬 서버 (표준 라이브러리)
│   └── index.html        # 단일 페이지 앱
└── dist/                 # 산출물 (gitignore)
```

## 설치

Python 3.9+ 와 패키지 3개(PyYAML · python-docx · python-pptx)가 필요하다. clone 후 한 번만:

```bash
pip install -r requirements.txt
```

> macOS/Linux/Windows 공통. 파일 입출력은 모두 UTF-8, 경로·한글 파일명(NFC)도 OS 무관하게 동작한다.

## 사용법

```bash
# 프로필 하나로 이력서 + 포트폴리오 조립
python build/build.py <profile-name>

# 예시
python build/build.py example-llm-eval
```

출력: `dist/<profile>/resume_<lang>.md`, `portfolio_<lang>.md`, `_report.md`

PDF 변환은 pandoc 사용 (선택):

```bash
pandoc dist/<profile>/resume_ko.md -o resume.pdf
```

## GUI (웹 편집·조립·Export)

브라우저에서 소스 편집 → 공고별 조립 → 미리보기 → Export까지 하는 로컬 도구.
서버는 파이썬 표준 라이브러리 + PyYAML 로 동작하고, `.docx` 내보내기는 python-docx 를 쓴다
(둘 다 `requirements.txt` 에 포함).

```bash
python app/server.py          # http://127.0.0.1:8765  (Chrome 권장)
```

- **소스 편집** 탭: `source/*.md`·`profiles/*.yaml`를 열어 편집·저장, 실시간 미리보기
- **공고 조립** 탭: emphasis(관점) 우선순위, 포함 경력·프로젝트를 체크로 선택. 각 프로젝트에
  현재 emphasis로 뽑힐 **뉘앙스(angle) 배지**가 실시간 표시. 프로필로 저장 가능.
- **미리보기 · Export** 탭: 이력서(고정 포맷)·포트폴리오(프로젝트별 페이지)를 렌더.
  인쇄/PDF 저장, `.doc`(Word), `.pptx`(PPT), `.html` 내려받기.
  - PPT는 가로(16:9) 슬라이드로, 프로젝트 1개 = 슬라이드 1장(문제 정의 → 나의 역할 → 주요 성과,
    분량에 맞춰 폰트가 자동으로 줄어들어 한 장에 다 들어간다). 다이어그램 이미지는 슬라이드 안에
    끼워 넣지 않고 프로젝트 슬라이드 바로 뒤에 이미지 전용 슬라이드로 분리한다.

## 진행 단계 (Phase)

- **Phase 1 — 뼈대** ✅ 폴더, vocab, 빌드/검증 스크립트, 소스 스켈레톤
- Phase 2 — 파일럿 1건 (p02 5축 평가 프레임워크 완성)
- Phase 3 — 정성 케이스 검증 (p12 데이터 구축·툴 개발)
- Phase 4 — LLM 보조 계층 (`assist.py`)
- Phase 5 — 확장
- Phase 6 — 조립 검증 (프로필 3종)

## 시드 출처

`source/` 의 fact/variant 초안은 사용자의 과거 이력서
(`example_cvs/` LinkedIn, Boeing/BCG 지원본)에서 추출했다.
날짜·수치·기여 범위는 `[확인필요]` 로 표시된 항목을 **사용자 재확인 후** 확정한다.
