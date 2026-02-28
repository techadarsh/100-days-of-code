from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game Part 1")

starting_position = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    new_segment.speed(0)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    time.sleep(0.2)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)

    if segments[0].xcor() > 280 or segments[0].xcor() < -280 or segments[0].ycor() > 280 or segments[0].ycor() < -280:
        game_is_on = False
        print("Game Over")









screen.exitonclick()