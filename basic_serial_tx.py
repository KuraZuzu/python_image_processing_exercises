import serial
import time

# シリアルポートの設定
port = "/dev/ttyACM0"  # Linuxの場合
# port = "COM3"  # Windowsの場合
baudrate = 115200

# シリアル通信のインスタンスを作成
ser = serial.Serial(port, baudrate, timeout=1)

# 送信する文字列
message = "Hello, STM32!"

try:
    while True:
        # メッセージをバイト型にエンコードして送信
        ser.write(message.encode())

        # データ送信後、少し待つ
        time.sleep(2)  # 2秒ごとにメッセージを送信

        # エコーバックされたデータの読み取り（オプション）
        while ser.in_waiting > 0:
            received_data = ser.read(ser.in_waiting)
            print("Received:", received_data.decode("utf-8"))

except KeyboardInterrupt:
    # Ctrl+Cが押された場合はループを終了
    print("Program terminated by user.")

finally:
    # シリアルポートを閉じる
    ser.close()
    print("Serial port closed.")
