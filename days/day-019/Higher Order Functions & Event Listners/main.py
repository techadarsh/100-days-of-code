from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

# Higher Order Functions
# below onkey() function is a higher order function as it takes another function as an argument

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()



