import serial
import time

# シリアルポートの設定
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
ser.flush()  # バッファをクリア

try:
    while True:
        # データを送信
        ser.write(b"Hello, microcontroller!\n")
        time.sleep(1)  # 少し待機（1秒間隔で送信）

        # データを受信（改行までの文字列を読み込む）
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").rstrip()  # 改行を削除
            print(f"Received: {line}")

except KeyboardInterrupt:
    print("通信を終了します")

finally:
    # シリアルポートを閉じる
    ser.close()
