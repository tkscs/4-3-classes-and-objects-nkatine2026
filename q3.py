class Calc_BC :
    """a group of children"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"A student named {self.name}"
    def speak(self):
        print(f"Mr. Katine, remember me, {self.name}? are you proud of me?")
Jordan = Calc_BC("Jordan")
Kyle = Calc_BC("Kyle")
Kyle.speak()
Jordan.speak()