import cv2

cap1 = cv2.VideoCapture(0)  # カメラデバイスの0番目を指定 "0" -> "/dev/video0"
cap2 = cv2.VideoCapture(4)  # カメラデバイスの0番目を指定 "0" -> "/dev/video0"

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1:  # フレーム取得ができなかったとき
        print("vide 1フレームを取得できません")
        break
    if not ret2:  # フレーム取得ができなかったとき
        print("video2 フレームを取得できません")
        break

    cv2.imshow("Camera 1", frame1)  # "Camera Feed"というウインドウを作成してカメラ表示
    cv2.imshow("Camera 2", frame2)  # "Camera Feed"というウインドウを作成してカメラ表示

    if cv2.waitKey(1) & 0xFF == ord("q"):  #"q"キーが押されたら
        break

cap1.release()  # カメラを開放する
cap2.release()  # カメラを開放する
cv2.destroyAllWindows()  # 作成したすべてのウインドウを閉じる