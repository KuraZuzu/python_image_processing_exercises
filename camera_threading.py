import cv2
import threading

frames = [None, None]  # 各カメラの最新フレームを保存する
running = [True, False]  # 各カメラのスレッドが動作しているかどうか

def capture_frame(camera_id, index):
    cap = cv2.VideoCapture(camera_id)

    if not cap.isOpened():
        print(f"Camera {camera_id} could not be opened.")
        running[index] = False  # カメラが開けなければ停止
        return

    while running[index]:
        ret, frame = cap.read()
        if not ret:
            print(f"Failed to grab frame from Camera {camera_id}.")
            running[index] = False
            break
        frames[index] = frame  # フレームを保存

    cap.release()

# カメラのスレッドを作成し、フレームを取得
thread1 = threading.Thread(target=capture_frame, args=(0, 0))
thread2 = threading.Thread(target=capture_frame, args=(4, 1))

thread1.start()
thread2.start()

# メインスレッドでフレームを表示
while any(running):
    if frames[0] is not None:
        cv2.imshow('Camera 0', frames[0])
    if frames[1] is not None:
        cv2.imshow('Camera 1', frames[1])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        running[0] = False
        running[1] = False
        break

# スレッドの終了を待機
thread1.join()
thread2.join()

cv2.destroyAllWindows()
