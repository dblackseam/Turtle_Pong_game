from turtle import Turtle

COLOR = "white"
SHAPE = "square"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(90)

    def go_up(self):
        self.forward(20)  # - my_approach - that is in my opinion way simpler and understandable than tutor's
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)

    def go_down(self):
        self.backward(20)  # - my_approach
        # new_y = self.ycor() - 20
        # self.goto(self.xcor(), new_y)
