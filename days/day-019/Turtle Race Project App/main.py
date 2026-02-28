from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
user_bat = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["purple", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = {}

def place_turtles():
    x = -350
    y = 150
    for color in colors:
        turtles[color+"-timmy"] = Turtle(shape="turtle")
        turtles[color+"-timmy"].penup()
        turtles[color+"-timmy"].color(color)
        turtles[color+"-timmy"].goto(x=x, y=y)
        y -= 50

place_turtles()

move_turtle_randomly = False
if user_bat:
    move_turtle_randomly = True

while move_turtle_randomly:
    for turtle in turtles:
        turtles[turtle].forward(random.randint(0,10))
        if turtles[turtle].xcor() > 350:
            move_turtle_randomly = False
            winning_color = turtle.split("-")[0]
            if winning_color == user_bat:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()