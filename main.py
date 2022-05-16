from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from net import Net
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Danil's Pong") 
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()
net = Net()
while net.ycor() != 300:
    net.draw_net()

screen.listen()
screen.onkeypress(key="Up", fun=paddle_r.go_up)
screen.onkeypress(key="Down", fun=paddle_r.go_down)
screen.onkeypress(key="w", fun=paddle_l.go_up)
screen.onkeypress(key="s", fun=paddle_l.go_down)

move = True
while move:
    screen.update()
    time.sleep(ball.move_speed)
    ball.drop()

    # Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() >= 330:
        ball.bounce_x()
    elif ball.distance(paddle_l) < 50 and ball.xcor() <= -330:
        ball.bounce_x()

    # Detect collision with walls behind the left/right paddle
    if ball.xcor() > 380:  # right paddle
        ball.reset_position()
        ball.bounce_x()
        score.add_to_an_l()

    elif ball.xcor() < -380:  # left paddle
        ball.reset_position()
        ball.bounce_x()
        score.add_to_an_r()

screen.exitonclick()
