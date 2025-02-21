from turtle import Turtle

class Turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0,-280)
    
    def move(self):
        self.forward(10)
    
    def back(self):
        self.backward(10)
    
    def startpoint(self):
        self.goto(0,-280)