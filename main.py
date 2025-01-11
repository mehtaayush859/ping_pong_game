from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
s.setup(width = 800, height = 600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

s.listen()
s.onkey(r_paddle.up, "Up")
s.onkey(r_paddle.down, "Down")
s.onkey(l_paddle.up, "w")
s.onkey(l_paddle.down, "s")

is_game_on = True
scoreboard.update_scoreboard()
while is_game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    
    #Detects the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detection collision with paddle
    if ball.distance(r_paddle) < 50 and  ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detects R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


s.exitonclick()


