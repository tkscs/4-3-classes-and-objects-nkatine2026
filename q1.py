class Cat:
    """a cat"""
    def speak():
        print("Meow!")

ella = Cat()
zoe = Cat()
print(ella)
print(zoe)


class Calc_BC :
    """a group of children"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"Mr. Katine, remember me, {self.name}? are you proud of me?")
Jordan = Calc_BC("Jordan")
Kyle = Calc_BC("Kyle")
Kyle.speak()
Jordan.speak()