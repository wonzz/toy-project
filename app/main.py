from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# [수정 포인트] 앱이 시작되기(start) 전에 미리 악기(Instrument)를 설치합니다.
# 이렇게 하면 앱 실행과 동시에 /metrics 엔드포인트가 생성됩니다.
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello, MSP Monitoring!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "success"}
