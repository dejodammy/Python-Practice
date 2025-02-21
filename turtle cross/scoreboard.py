FONT = ("Courier", 12, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup() 
        self.level = 1
        self.goto(-280,250)
        self.write(f"level: {self.level}", "center", font= FONT)
    
    def game_over(self):
        self.clear()
        self.goto(-50,0)
        self.write(f"GAME OVER", "center", font= FONT)
        self.goto(-280,250)
        self.write(f"level: {self.level}", "center", font= FONT)   
    
    def win(self):
        self.clear()
        self.level += 1
        self.goto(-280,250)
        self.write(f"level: {self.level}", "center", font= FONT)        
    
