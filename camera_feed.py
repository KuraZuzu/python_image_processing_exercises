import sys
import cv2

args = sys.argv
camera_id = int(args[1])

cap = cv2.VideoCapture(camera_id)  # カメラデバイスの0番目を指定
while True:
    ret, frame = cap.read()
    if not ret:  # フレーム取得ができなかったとき
        print("フレームを取得できません")
        break

    cv2.imshow("Camera Feed", frame)  # "Camera Feed"というウインドウを作成してカメラ表示
    if cv2.waitKey(1) & 0xFF == ord("q"):  #"q"キーが押されたら
        break

cap.release()  # カメラを開放する
cv2.destroyAllWindows()  # 作成したすべてのウインドウを閉じる
