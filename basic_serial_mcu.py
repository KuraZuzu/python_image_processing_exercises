import serial

# シリアルポートの設定
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
ser.flush()  # バッファをクリア

# データを送信
ser.write(b"Hello, microcontroller!\n")

# データを受信（改行までの文字列を読み込む）
if ser.in_waiting > 0:
    line = ser.readline().decode("utf-8".rstrip)  # 改行を削除
    print(f"Received: {line}")

# シリアルポートを閉じる
ser.close()
