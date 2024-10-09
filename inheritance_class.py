class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # 今はなにもしない処理だが、継承先のサブクラスで実装

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof !")

dog = Dog("Buddy")
dog.speak()