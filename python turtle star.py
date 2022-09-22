
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(10)

def sqrfunc(size):
    for x in range(100):
        t.pencolor(colors[x%6])
        t.fd(size)
        t.right(144)
        size = size + 5

sqrfunc(1)
turtle.done()