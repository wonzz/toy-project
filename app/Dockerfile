# 1. 파이썬 3.12 슬림 버전 사용 (가볍고 빠름)
FROM python:3.12-slim

# 2. 컨테이너 내부의 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 라이브러리 설치 (경고 났던 그 라이브러리들!)
RUN pip install --no-cache-dir fastapi uvicorn prometheus-fastapi-instrumentator

# 4. 현재 폴더의 모든 파일(main.py 등)을 컨테이너로 복사
COPY . .

# 5. 앱 실행 (8000번 포트로 대기)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
