from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
up, down, left, right = 90, 270, 180, 0


class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        body = Turtle("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.snake.append(body)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            new_goto = (self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
            self.snake[i].goto(new_goto)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
