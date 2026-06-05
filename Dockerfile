# 1. 파이썬 3.11 환경 기반
FROM python:3.11-slim

# 2. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /app

# 3. 시스템 의존성 및 빌드 도구 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. 소스 코드 및 설정 파일 전체를 컨테이너 내부(/app)로 복사
# (이렇게 해야 Model_params, model_config.json, Website_detector가 통째로 잘 들어갑니다.)
COPY . /app

# 5. setup.py를 이용해 의존성 패키지 일괄 설치
RUN pip install --no-cache-dir -e .

# 6. Playwright 리눅스 브라우저 환경 및 바이너리 설치
RUN playwright install --with-deps chromium

# 7. 외부 사용자가 접속할 수 있도록 FastAPI 포트 개방
EXPOSE 8080

# 🔥 8. [수정 완료] uvicorn이 하위 폴더(Website_detector) 내부의 앱을 인식할 수 있도록 경로 변경!
# "Website_detector.UI_Window:app" 으로 지정해 주어야 모듈 탐색 에러가 나지 않습니다.
CMD ["uvicorn", "Website_detector.UI_Window:app", "--host", "0.0.0.0", "--port", "8080"]