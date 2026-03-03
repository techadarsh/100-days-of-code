from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() > 230:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() < -230:
            new_y = self.ycor()
        self.goto(self.xcor(), new_y)