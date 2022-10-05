import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors_list = [
    (202, 5, 72),
    (198, 164, 10),
    (235, 51, 129),
    (206, 76, 11),
    (108, 179, 218),
    (219, 162, 103),
    (234, 225, 6),
    (30, 188, 108),
    (23, 106, 173),
    (13, 23, 64),
    (17, 28, 175),
    (213, 135, 176),
    (9, 185, 214),
    (205, 29, 142),
    (229, 168, 197),
    (125, 189, 162),
    (8, 49, 28),
    (37, 132, 73),
    (125, 219, 233),
    (67, 22, 8),
    (61, 11, 26),
    (111, 89, 211),
    (142, 216, 201),
    (190, 15, 5),
    (238, 63, 31)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for i in range(100):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if (i + 1) % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

turtle.Screen().exitonclick()
