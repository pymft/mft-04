import turtle


print(type(turtle.Turtle))

class NewTurtle(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed(8)

    #     self.buddy = None
    #
    # def set_buddy(self, other):
    #     self.buddy = other
    #
    # def come_closer(self):
    #     pass

    def turn(self):
        for i in range(4):
            self.forward(100)
            self.left(90)


nt1 = NewTurtle()
nt2 = NewTurtle()

# nt1.set_buddy(nt2)

nt1.left(10)
nt1.forward(10)

print(nt1.pos())

