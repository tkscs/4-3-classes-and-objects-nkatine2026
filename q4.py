import turtle
constant = 2
c1 = 0.99
c2 = 0.99
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.w = x*constant
        self.z = x*constant
    def draw(self):
        turtle.goto(self.x, self.y)
    def scale(self, constant):
        self.x = self.x * constant
        self.y = self.y * constant
    def draw2(self):
        turtle.goto(self.w, self.z)
    def __str__(self):
        return f"({self.x}, {self.y})"
    def sheer(self):
        self.wa = self.x*c1**i
        self.za = self.y*c2**i
    def drawboogalo(self):
        turtle.goto(self.wa, self.za)
    
p1 = Point(0,0)
p2 = Point(100, 0)
p3 = Point(100, 100)
p4 = Point(0,100)
p2.draw()
p3.draw()
p4.draw()
p1.draw()
for i in range(297):
    p2.sheer()
    p3.sheer()
    p4.sheer()
    p1.sheer()
    p2.drawboogalo()
    p3.drawboogalo()
    p4.drawboogalo()
    p1.drawboogalo()








turtle.exitonclick()