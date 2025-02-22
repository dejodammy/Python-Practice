from turtle import Turtle
POSITION =[(0,0),(-20,0),(-40,0)]
STEPS = (20)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.Snakes = []
        self.create_snake()
        self.head = self.Snakes[0]
        
    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)
    
    
    def add_segment(self,position):    
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(position)
        self.Snakes.append(turtle)    
        
    def reset(self):
        for seg in self.Snakes:
            seg.goto(1000,1000)
        self.Snakes.clear()
        self.create_snake()
        self.head = self.Snakes[0]
        
    def extend(self):
        self.add_segment(self.Snakes[-1].position())
            
    def move(self):
        for seg in range(len(self.Snakes) -1, 0 , -1):
            new_x = self.Snakes[seg - 1 ].xcor()
            new_y = self.Snakes[seg - 1 ].ycor()
            self.Snakes[seg].goto(new_x,new_y)
        self.head.forward(STEPS)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)