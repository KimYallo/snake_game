from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_s = []
        self.create_snake()
        self.head = self.snake_s[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.goto(position)
        self.snake_s.append(snake)

    def reset(self):
        for s in self.snake_s:
            s.hideturtle()
        self.snake_s.clear()
        self.create_snake()
        self.head = self.snake_s[0]

    def extend(self):
        # add a new segment to the snake.
        self.add_snake(self.snake_s[-1].position())

    def move(self):
        for s_num in range(len(self.snake_s) - 1, 0, -1):
            new_x = self.snake_s[s_num - 1].xcor()
            new_y = self.snake_s[s_num - 1].ycor()
            self.snake_s[s_num].goto(new_x, new_y)

        self.snake_s[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
