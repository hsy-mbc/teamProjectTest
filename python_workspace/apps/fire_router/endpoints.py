# 웹소캣을 통한 데이터 전송
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    pass


@app.post()
async def fire_api():
    pass