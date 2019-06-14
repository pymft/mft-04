import turtle


def recursive_turtle(t, n, angle):
    if n < 15:
        return
    t.forward(n)
    t.left(angle)
    recursive_turtle(t, n, angle*1.01)


t =turtle.Turtle()
recursive_turtle(t, 100, 90)
