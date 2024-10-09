class Dog:

    # コンストラクタの定義
    def __init__(self, name, bread):
        # インスタンス変数（属性）
        self.name = name
        self.bread = bread

    # メソッド（動作）
    def bark(self):
      print(f"{self.name} says Woof !")

my_dog = Dog("Buddy", "Chiwawa")
my_dog.bark()