import serial
from time import sleep
from dataclasses import dataclass
from enum import Enum

# 定数として必要な情報を定義
PORT = '/dev/ttyACM0'  # シリアルポートのデバイス名
BAUDRATE = 115200      # ボーレート
TIMEOUT = 1.0          # タイムアウト時間（秒）

class RobotStateId(Enum):
    STATE_IDLE = 0
    STATE_ACTIVE = 1
    # 必要に応じて他の状態を追加

@dataclass
class RobotState:
    state_id: RobotStateId = RobotStateId.STATE_IDLE
    ready_to_fire: bool = False
    pitch_deg: float = 0.0
    muzzle_velocity: float = 0.0
    record_video: bool = False
    reboot_pc: bool = False
    num_disks: int = 0
    video_id: int = 0

def main():
    try:
        # シリアルポートを開く
        ser = serial.Serial(
            port=PORT,
            baudrate=BAUDRATE,
            parity=serial.PARITY_NONE,
            timeout=TIMEOUT,
        )
        print(f"Opened serial port: {PORT}")
    except serial.serialutil.SerialException as err:
        print(f"Failed to open serial port: {err}")
        return

    robot_state = RobotState()

    try:
        while True:
            # 改行コードまでデータを読み取る
            buffer = ser.readline()
            send_msg = "540,360,0,0\n"
            ser.write(send_msg.encode())
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
                robot_state = RobotState(
                    state_id=RobotStateId(int(str_data_list[0])),
                    ready_to_fire=bool(int(str_data_list[1])),
                    pitch_deg=float(str_data_list[2]) / 10.0,         # 1/10度単位を度に変換
                    muzzle_velocity=float(str_data_list[3]) / 1000.0, # mm/sをm/sに変換
                    record_video=bool(int(str_data_list[4])),
                    reboot_pc=bool(int(str_data_list[5])),
                    num_disks=int(str_data_list[6]),
                    video_id=int(str_data_list[7]),
                )
                print(robot_state)
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
