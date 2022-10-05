from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=960, height=540)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a clolor: ")
colors = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
all_turtles = []


for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-460, y=(150 - i*50))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 460:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost... The {turtle.pencolor()} turtle is the winner!")
        else:
            turtle.forward(random.randint(0, 10))

screen.exitonclick()
