from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake game")


screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:     
    screen.update() 
    time.sleep(0.1) 
    snake.move()
    
    if snake.head.distance(food) < 15:
        scoreboard.keep_score()
        snake.extend()
        food.move()
        
        
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_overself()
        game_on = False
    
    for segment in snake.Snakes[1:]:     
        if snake.head.distance(segment) < 10:            
            scoreboard.game_overself()
            game_on = False            
            
    

screen.exitonclick()