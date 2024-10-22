import cv2
import threading

frames = [None, None]  # 各カメラの最新フレームを保存する
running = [True, True]  # 各スレッドの状態を管理
current_camera = 0  # 表示するカメラのインデックス（0 or 1）
lock = threading.Lock()  # スレッド間での競合を防ぐロック

def capture_frame(camera_id, index):
    """カメラからフレームを取得し続けるスレッド処理"""
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

        with lock:  # フレームの書き込みをロックで保護
            frames[index] = frame

    cap.release()

# 2つのカメラ用のスレッドを作成し、開始する
thread1 = threading.Thread(target=capture_frame, args=(0, 0))
thread2 = threading.Thread(target=capture_frame, args=(4, 1))

thread1.start()
thread2.start()

# メインスレッドでフレームを表示し、スペースキーで切り替える
while any(running):
    with lock:  # 現在表示するカメラのフレームを取得
        frame = frames[current_camera]

    if frame is not None:
        cv2.imshow('Camera Viewer', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # 'q'キーで終了
        running[0] = False
        running[1] = False
        break
    elif key == ord(' '):
        # スペースキーで表示するカメラを切り替える
        current_camera = (current_camera + 1) % 2  # 0 <-> 1 の切り替え

# スレッドの終了を待機
thread1.join()
thread2.join()

cv2.destroyAllWindows()
