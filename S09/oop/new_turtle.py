import turtle
import math
from random import randint

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
        path = math.sqrt((dx ** 2 + dy ** 2)) // 3
        t = math.atan2(dy, dx)
        d = math.degrees(t)
        self.setheading(d)
        self.__dude.setheading(180 + d)
        self.forward(path)
        self.dude.forward(path)

    def random_walk(self):
        self.left(randint(0, 360))
        self.forward(randint(10, 100))


nt1 = NewTurtle()
nt2 = NewTurtle()
nt3 = NewTurtle()
nt4 = NewTurtle()

nt1.color((1, 0, 0))
nt2.color((1, 0, 0))

nt2.dude = nt1
nt4.dude = nt3

for i in range(10):
    for nt in [nt1, nt3]:
        nt.random_walk()
        nt.come_closer()


