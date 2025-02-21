from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")      
        self.xmove = 3
        self.ymove = 3 
        self.move_speed = 0.1
        
    def move(self):
        x_cor = self.xcor() + self.xmove
        y_cor = self.ycor()+ self.ymove
        self.goto(x_cor,y_cor)
    
    def bounce_y(self):
        self.ymove *= -1
        self.move_speed *= 0.9
    
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

        
    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

