from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")

        
        
    def move(self):
        x_place = random.randint(-290,290)
        y_place = random.randint(-290,290)
        self.goto(x_place, y_place)        

