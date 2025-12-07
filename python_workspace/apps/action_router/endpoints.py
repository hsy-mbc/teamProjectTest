# 웹소캣을 통한 데이터 전송
from fastapi import FastAPI
from camera import camera_connect, camera_disconnect

app = FastAPI()


@app.get("/")
async def index():
    pass


@app.get()
async def camera_image_get_api():
    cap = camera_connect()

    camera_disconnect(cap)
    pass


@app.post()
async def action_api():
    pass