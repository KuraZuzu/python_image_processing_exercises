def greet(name):
    print(f"Hello, {name} !")

def add(a, b):
    return a + b

# 数字のリストを表示する関数
def print_numbers(numbers):
    for number in numbers:
        print(number)

greet("Alice")
greet("Zuzu")
print(add(12, 16))

number_list = [1, 3, 5, 3, 4]
print_numbers(number_list)
