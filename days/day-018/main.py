from turtle import Turtle, Screen

timmy_turtle = Turtle()

timmy_turtle.shape("turtle")
timmy_turtle.color("red")
timmy_turtle.left(90)
timmy_turtle.forward(100)

# Challange 1 - Draw a square
tim = Turtle()
tim.shape("turtle")
tim.color("blue")
for i in range(0,4):
    tim.forward(100)
    tim.right(90)

# Importing Modules, Installing Packages, and Working with Aliases
# import tutle
# from turtle import Turtle, Screen
# from turtle import *

# # Aliasing Modules
# import turtle as t
# tim = t.Turtle()

# installing packages
# pip install heroes
import heroes as h

print(h.gen())


# Challange 2 - Draw a dashed line

dash_tim = Turtle()
dash_tim.shape("turtle")
dash_tim.color("green")
dash_tim.left(180)
for i in range(0,15):
    dash_tim.forward(10)
    dash_tim.penup()
    dash_tim.forward(10)
    dash_tim.pendown()

# Challange 3 - Draw different shapes
import random
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
shapes_tim = Turtle()
shapes_tim.shape("turtle")
shapes_tim.color("purple")
shapes_tim.speed("fastest")
for i in range(3,11):
    shapes_tim.color(random.choice(colors))
    for j in range(0,i):
        shapes_tim.forward(100)
        shapes_tim.right(360/i)


# Challenge 4 Generate A Random Walk
# continue this with tuple and random RGB color generation
# walk_tim = Turtle()
# walk_tim.penup()
# walk_tim.left(90)
# walk_tim.forward(500)
# walk_tim.pendown()
# walk_tim.shape("turtle")
# walk_tim.color("black")
# walk_tim.pensize(15)
# walk_tim.speed("fastest")
# directions = [0,90,180,270]
# for i in range(0,500):
#     walk_tim.color(random.choice(colors))
#     walk_tim.setheading(random.choice(directions))
#     walk_tim.forward(50)

# Python Tuples and How to generate Random RGB colors
# Description of Tuple
# Tuples are a data structure in Python that is similar to lists, but they are immutable,
# meaning that once a tuple is created, its elements cannot be changed.
# Tuples are defined using parentheses () and can contain a sequence of values
# of any type. They are often used to group related data together and
# can be accessed using indexing, just like lists. However,
# since tuples are immutable, they do not have methods that modify the data,
# such as append() or remove(). Instead,
# you can create a new tuple by concatenating existing tuples
# or by using the tuple() constructor.

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color_tuple = (r, g, b)
    return random_color_tuple

import turtle as t
t.colormode(255)
walk_tim = t.Turtle()
walk_tim.penup()
walk_tim.left(90)
walk_tim.forward(250)
walk_tim.pendown()
walk_tim.shape("turtle")
walk_tim.color((0,0,0))
walk_tim.pensize(15)
walk_tim.speed("fastest")
directions = [0,90,180,270]
for i in range(0,200):
    walk_tim.color(random_color())
    walk_tim.setheading(random.choice(directions))
    walk_tim.forward(50)


# Challenge 5 - Draw a Spirograph
circle_tim = t.Turtle()
circle_tim.shape("turtle")
circle_tim.speed("fastest")
circle_tim.penup()
circle_tim.forward(200)
circle_tim.pendown()
circle_tim.color(random_color())
for i in range(0,72):
    circle_tim.color(random_color())
    circle_tim.circle(150)
    circle_tim.setheading(circle_tim.heading() + 5)


screen = Screen()
screen.exitonclick()