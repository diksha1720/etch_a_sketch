from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def forward():
    tim.forward(30)


def backward():
    tim.backward(30)


def counter_clock():
    tim.left(10)


def clock():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()