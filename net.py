from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(10)
        self.penup()
        self.goto(x=0, y=-300)

    def draw_net(self):
        self.setheading(90)
        self.penup()
        self.forward(30)
        self.pendown()
        self.forward(30)

