from turtle import Screen , Turtle
from turtles import Turtles
from scoreboard import Scoreboard
import time
from car_manager import CarManager

screen = Screen()
screen.bgcolor("white")
screen.setup(600,600)
screen.title(" Turtle cross ")
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()




turtles = Turtles()

screen.listen()
screen.onkey(turtles.move, "Up")
screen.onkey(turtles.back, "Down")

is_play = True
while is_play:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    
    for car in car_manager.all_cars:
        if car.distance(turtles) < 20:
            scoreboard.game_over()
            is_play = False
    if turtles.ycor() > 300:
        turtles.startpoint()
        scoreboard.win()
        



screen.exitonclick()