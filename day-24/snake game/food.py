from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        new_goto = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(new_goto)
        self.refresh()

    def refresh(self):
        new_goto = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(new_goto)
