import turtle
import math


print(type(turtle.Turtle))


class NewTurtle(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed(8)
        self.__dude = None

    @property
    def dude(self):
        return self.__dude

    @dude.setter
    def dude(self, value):
        self.__dude = value
        if self.dude.dude != self:
            self.dude.dude = self

    def turn(self):
        for i in range(4):
            self.forward(100)
            self.left(90)

    def come_closer(self):
        x1, y1 = self.pos()
        x2, y2 = self.__dude.pos()
        dx = x2 - x1
        dy = y2 - y1
        t = math.atan2(dy, dx)
        d = math.degrees(t)
        self.setheading(d)
        self.__dude.setheading(180 + d)



nt1 = NewTurtle()
nt2 = NewTurtle()

nt2.dude = nt1

