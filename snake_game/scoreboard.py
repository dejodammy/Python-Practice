from turtle import Turtle
ALIGNMENT = "center"
FONT = ("coriel", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.hideturtle()
        self.update_score()
        
        
    def update_score(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)
        
    def game_overself(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over Score: {self.score}", align= ALIGNMENT, font= FONT)

        
        
    def keep_score(self):
        self.score += 1
        self.clear()
        self.update_score()