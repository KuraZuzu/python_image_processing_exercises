import cv2

cap = cv2.VideoCapture("/dev/video8")  # カメラデバイスの0番目を指定
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