# 프로젝트 다이어그램 / 이미지

포트폴리오 각 프로젝트 카드의 "이미지 / 다이어그램 자리"에 들어가는 파일 위치입니다.

## 동작 방식

프로젝트 id → 파일명 매핑이 `app/index.html` 의 `DIAGRAMS` 상수에 정의돼 있습니다.
프론트엔드는 이 매핑을 보고 `assets/diagrams/<파일명>` 을 불러와 placeholder(🖼)를 교체합니다.
파일이 없으면 placeholder 가 그대로 유지됩니다.

```js
const DIAGRAMS={
  p01:['ai voice system architecture.png'],
  p05:['Cephalometric Landmark Detection.png'],
  p08:['Text2SQL Product UI.png','Text2SQL System Architecture.png','DARVIS DB통합.png'],   // 프로젝트당 여러 장 가능
  p09:['RAG architecture.png'],
  p11:['Auto positioning.jpg'],
  p12:['panorama labeling tool.png'],
  p13:['Dental Panoramic Radiograph Segmentation.png']
};
```

## 현재 매핑

| 프로젝트 | 파일 |
|---|---|
| p01 · C-arm 음성 제어 | `ai voice system architecture.png` |
| p05 · Cephalo 랜드마크 | `Cephalometric Landmark Detection.png` |
| p08 · Text-to-SQL (DARVIS) | `Text2SQL Product UI.png`, `Text2SQL System Architecture.png`, `DARVIS DB통합.png` |
| p09 · RAG 챗봇 | `RAG architecture.png` |
| p11 · 오토포지셔닝 | `Auto positioning.jpg` |
| p12 · 어노테이션 툴 | `panorama labeling tool.png` |
| p13 · Panoramic 분할 | `Dental Panoramic Radiograph Segmentation.png` |

> `DARVIS RAG Product UI.png` 는 아직 어느 프로젝트에도 매핑돼 있지 않습니다 (p08/p09 중 어디에 붙일지
> 애매해 자동으로 넣지 않았습니다) — 필요하면 위 표와 `DIAGRAMS` 상수에 직접 추가해주세요.

## 이미지 추가 / 교체

1. 파일을 이 폴더(`assets/diagrams/`)에 넣습니다. (파일명에 공백·한글 사용 가능)
2. `app/index.html` 의 `DIAGRAMS` 에 `프로젝트id: ['파일명', ...]` 항목을 추가·수정합니다.
   - 한 프로젝트에 여러 장을 넣으면 카드에 세로로 나란히 표시됩니다.
3. 브라우저에서 미리보기 탭을 새로고침(다시 조립 or 언어 재선택)하면 반영됩니다.

## 팁

- 프로젝트 카드 썸네일(갤러리)에는 첫 번째 이미지가 대표 이미지로 표시됩니다.
- 이미지에는 별도의 캡션을 표시하지 않습니다 (alt 텍스트만 내부적으로 유지).
- 이미지 클릭 시 새 탭에서 원본이 열립니다.
- 가로로 긴 다이어그램은 카드 폭에 맞춰 자동 축소됩니다. 가독성을 위해 **가로 1200~1600px** 권장.
- 지원 형식: `png` · `jpg` · `jpeg` · `webp` · `svg` · `gif`.
