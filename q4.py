import turtle
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        turtle.goto(self.x, self.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(0,0)
p2 = Point(100, 0)
p3 = Point(100, 100)
p4 = Point(0,100)
p2.draw()
p3.draw()
p4.draw()
p1.draw()










turtle.exitonclick()