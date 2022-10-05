from ctypes.wintypes import RGB
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
# tim.shape("turtle")
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spiograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

# direction = []

# for i in range(30):
#     direction.append(i * 12)

# for i in range(30):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(direction[i])

draw_spiograph(1)

screen = turtle.Screen()
screen.exitonclick()
