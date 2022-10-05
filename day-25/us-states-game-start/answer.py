from tkinter import CENTER
from turtle import Turtle


class AnswerBoard(Turtle):

    def __init__(self, new_goto, answer) -> None:
        super().__init__()
        self.penup()
        self.goto(new_goto)
        self.write(answer, align="center")
        self.hideturtle()
