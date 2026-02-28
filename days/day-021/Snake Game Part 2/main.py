# starting this approach with OOP
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
user_name = screen.textinput(title="Enter your name", prompt="Please enter your name to start the game: ")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
score = ScoreBoard(user_name)

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail using slice
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()