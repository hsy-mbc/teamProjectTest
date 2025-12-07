# 행동 감지 모델 탑재 - json 파일로 변환
import cv2


def action_model_video(cap):

    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임 받기 실패")
            break

        cv2.imshow('IP Webcam Live', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return cv2


def action_objects():
    result_image = ""
    return result_image