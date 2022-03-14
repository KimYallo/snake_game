from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# make screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# make snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        # print("nom nom nom")
        scoreboard.show_score()
        food.refresh()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
        scoreboard.show_score()

    # Detect collision with tail.
    for s in snake.snake_s[1:]:
        if snake.head.distance(s) < 10:
            scoreboard.reset()
            snake.reset()
            scoreboard.show_score()
    # if head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()
