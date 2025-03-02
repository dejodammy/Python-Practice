from turtle import Screen 
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

    
    
    
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()



    
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed) 
    screen.update()
    ball.move()   
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #ball miss right
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.lpoint()

    
    #ball miss left
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.rpoint()  
    
    
screen.exitonclick() 