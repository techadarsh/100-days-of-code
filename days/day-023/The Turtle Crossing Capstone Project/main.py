"""
The Turtle Crossing Capstone Project
1. Create the Screen
2. Create and move the turtle
3. Create and move the cars
4. Detect collision with car
5. Detect successful crossing
6. Keep score
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=800)
screen.tracer(0)
car = CarManager()
score = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # detect collision with car
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car.level_up()
        score.increase_score()

screen.exitonclick()