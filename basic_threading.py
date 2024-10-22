import threading

def print_numbers():
    for i in range(4):
        print(f"Numbler: {i}")

def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"Letter: {letter}")

# スレッドの作成
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# スレッドの開始
thread1.start()
thread2.start()

# 全てのスレッドの完了を待つ
# thread1.join()
# thread2.join()

print("Bothe threads finished.")