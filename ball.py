from turtle import Turtle

SHAPE = 'circle'
COLOR = 'white'


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def drop(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def bounce_y(self):
        self.y *= -1   # change is happening according to its location (y), if y is positive then it's going to be
        #  negative

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1  # in order to update the speed each time the ball flies out of the gates
        self.goto(0, 0)
