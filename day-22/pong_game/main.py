from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

Screen().setup(800, 600)
Screen().bgcolor("black")
Screen().title("Pong")
Screen().tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


Screen().listen()
Screen().onkey(r_paddle.up, "Up")
Screen().onkey(r_paddle.down, "Down")
Screen().onkey(l_paddle.up, "w")
Screen().onkey(l_paddle.down, "s")

while True:
    Screen().update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


Screen().exitonclick()
