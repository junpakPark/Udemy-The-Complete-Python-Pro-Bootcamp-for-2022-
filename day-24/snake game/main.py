from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

Screen().setup(width=600, height=600)
Screen().bgcolor("black")
Screen().title("Snake Game")
Screen().tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

Screen().listen()
Screen().onkey(snake.up, "Up")
Screen().onkey(snake.down, "Down")
Screen().onkey(snake.left, "Left")
Screen().onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    Screen().update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for body in snake.snake[1:]:
        if snake.head.distance(body) < 15:
            snake.reset()

Screen().exitonclick()
