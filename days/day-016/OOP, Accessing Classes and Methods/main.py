"""
How to import another module
"""
import another_module
print(another_module.another_variable)

# Constructing Objects
# import turtle
# in below line timmy_1 is object and Tutle() is class (blueprint)
# timmy_1 = turtle.Turtle() # to construct the blueprint we have to add brackets

#  second way to import class
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle") # method
timmy.color("coral") # method
timmy.forward(100) # method

# Object Attributes
my_screen = Screen()
print(my_screen.canvheight) # Object.attribute

# Objects Methods
my_screen.exitonclick() # object.method

