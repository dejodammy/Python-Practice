""" Turtle drawing movements"""

# from turtle import Turtle, Screen

# tim = Turtle()
# tim.shape("turtle")

# def up_key():
#     tim.forward(20)
    
# def left_key():
#     tim.left(10)


# def right_key():
#     tim.right(10)


# def down_key():
#     tim.forward(20)

# def clear_screen():
#     tim.clear()

# screen = Screen()

# screen.onkey(up_key,"Up")
# screen.onkey(left_key,"Left")
# screen.onkey(right_key,"Right")
# screen.onkey(down_key,"Down")
# screen.onkey(clear_screen,"c")


# screen.listen()
# screen.exitonclick()

""" Turtle Betting Race """

# from turtle import Turtle, Screen
# import random

# screen = Screen()
# screen.setup(500,400)

# class TurtlePlayers:
#     def __init__(self, name, color):
#         self.name_string = name  
#         self.color = color
#         self.turtle = Turtle()
#         self.turtle.color(self.color)
#         self.turtle.shape("turtle")
#         self.turtle.penup()
#         self.turtle.setpos(-230, 0)
#         self.race_finished = False  

#     def move(self):
#         while not self.race_finished:
#             self.turtle.forward(random.randint(1, 5))
#             self.check_winner()
#             screen.ontimer(self.move, 100)  
#             break
        

#     def check_winner(self):
#         x, _ = self.turtle.position()
#         if x > 500 and not self.race_finished:  
#             print(f"{self.name_string} won the race!")


# winner = screen.textinput("TURTLE BET", "What color do you think is winning?")
# print(winner)

# tim = TurtlePlayers("Timmy", "blue")
# tim.move()  


# turtle2 = TurtlePlayers("Tina", "red")
# turtle2.move()

# screen.exitonclick()


""" Turtle Betting Race """

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)


winner = screen.textinput("TURTLE BET", "What color do you think is winning?")
colors = ["red","blue","green","orange","yellow"]
y_pos = [-70,-40,-10,20,50]
turtles = []

for turtle_index in range(0,5):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.goto(x = -230,y = y_pos[turtle_index])
        new_turtle.color(colors[turtle_index])
        turtles.append(new_turtle)
        
def check_winner():
    x , _ = new_turtle.pos
    if x >= 500:
        print(f"Color {new_turtle.color} won")

if winner:
    is_race = True
    while is_race:
        for t in turtles:
            t.forward(random.randint(0,10))
        
        
        
screen.exitonclick()
