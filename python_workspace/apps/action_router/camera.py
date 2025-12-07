# ip 카메라 연동

# ipcam - mqtt api 활용
# 모스키토 환경설정 변경 "C:\Program Files\mosquitto\mosquitto.conf"
import cv2
import os
from dotenv import load_dotenv
from common.config import CameraPath


def camera_connect():
    CP = CameraPath

    url = f"http://{CP.WEBCAM_ID}:{CP.WEBCAM_PW}@{CP.WEBCAM_IP}:{CP.WEBCAM_PORT}/video"
    print(f"Webcam 연결중 : {url}")

    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        exit()

    return cap


def camera_disconnect(cap):
    cap.release()
    cv2.destroyAllWindows()
    return "cap, cv2 종료 되었습니다."


def camera_api():
    return 'rtsp://admin:AI!!3203@192.168.0.14:554'