class Animal:
    def __init__(self):
        self.no_eyes = 2
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.no_legs = 4
    def breathe(self):
        super().breathe()
        print("Dog is breathing")

    def bark(self):
        print("Woof!")

memo=Dog()
memo.bark()
print(memo.no_legs)
print(memo.no_eyes)
memo.breathe()
