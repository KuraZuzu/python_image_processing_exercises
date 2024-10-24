import serial
from time import sleep
from dataclasses import dataclass

# 定数として必要な情報を定義
PORT = '/dev/ttyACM0'  # シリアルポートのデバイス名
BAUDRATE = 115200      # ボーレート
TIMEOUT = 1.0          # タイムアウト時間（秒）


@dataclass
class RobotState:
    robot_state: int = 0          # ロボット状態
    pitch_deg: float = 0.0        # ピッチ角度
    muzzle_velocity: float = 0.0  # 射出速度
    left_frisbee_count: int = 0   # 左フリスビー枚数
    right_frisbee_count: int = 0  # 右フリスビー枚数
    camera_id: int = 0            # カメラID
    flag: int = 0                 # フラグ
    reserved: int = 0             # 予備


def main():
    try:
        # シリアルポートを開く
        ser = serial.Serial(
            port=PORT,
            baudrate=BAUDRATE,
            parity=serial.PARITY_NONE,
            # parity=serial.PARITY_EVEN,
            timeout=TIMEOUT,
        )
        print(f"Opened serial port: {PORT}")
    except serial.serialutil.SerialException as err:
        print(f"Failed to open serial port: {err}")
        return

    try:
        while True:
            # 改行コードまでデータを読み取る
            buffer = ser.readline()
            if not buffer:
                continue  # タイムアウトの場合は次のループへ

            # データをASCIIでデコード
            try:
                str_data = buffer.decode("ascii").strip()
            except UnicodeDecodeError as err:
                print(f"Decode error: {err}")
                continue

            # データをパース
            try:
                str_data_list = str_data.split(",")
                if len(str_data_list) < 8:
                    print("Incomplete data received")
                    continue

                robot_state = RobotState(
                    robot_state=int(str_data_list[0]),
                    pitch_deg=float(str_data_list[1]),
                    muzzle_velocity=float(str_data_list[2]),
                    left_frisbee_count=int(str_data_list[3]),
                    right_frisbee_count=int(str_data_list[4]),
                    camera_id=int(str_data_list[5]),
                    flag=int(str_data_list[6]),
                    reserved=int(str_data_list[7]),
                )

                # 値を表示
                print(f"ロボット状態: {robot_state.robot_state}")
                print(f"ピッチ角度: {robot_state.pitch_deg}")
                print(f"射出速度: {robot_state.muzzle_velocity}")
                print(f"左フリスビー枚数: {robot_state.left_frisbee_count}")
                print(f"右フリスビー枚数: {robot_state.right_frisbee_count}")
                print(f"カメラID: {robot_state.camera_id}")
                print(f"フラグ: {robot_state.flag}")
                print(f"予備: {robot_state.reserved}")
                print("----------------------------")
            except (ValueError, IndexError) as err:
                print(f"Parsing error: {err}")
                continue

            # 適度に待機
            sleep(0.1)
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        ser.close()
        print("Closed serial port")

if __name__ == "__main__":
    main()
