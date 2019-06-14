import turtle


def turn(t, length, initial_angle=0):
    t.left(initial_angle)
    for i in range(4):
        t.forward(length)
        t.left(90)


def star(t, angle=10):
    for i in range(0, 100, angle):
        turn(t, 90, initial_angle=i)


t2 = turtle.Turtle()
t1 = turtle.Turtle()
t1.speed(10)
t2.speed(10)
star(t1, angle=15)
star(t2, angle=10)


