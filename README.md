# 이력서 분석 및 처우 분석 시스템

이 프로젝트는 이력서 데이터를 분석하고 처우 정보를 시각화하는 Streamlit 기반 웹 애플리케이션입니다.

## 주요 기능

- 이력서 데이터 분석
  - 데이터 미리보기
  - 기본 통계 분석
  - 경력 및 학력 분포 시각화

- 처우 분석
  - 연령대별 평균 연봉 분석
  - 경력과 연봉의 상관관계 분석

## 설치 방법

1. 저장소 클론
```bash
git clone [repository-url]
cd hr-rec
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

## 실행 방법

```bash
streamlit run app.py
```

## 데이터 형식

이력서 분석을 위한 CSV 파일은 다음 컬럼을 포함해야 합니다:
- 경력
- 학력
- 기타 관련 정보

## 라이선스

MIT License 