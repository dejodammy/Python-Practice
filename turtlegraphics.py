""" TURTLE POLYGONS """
# from turtle import Turtle , Screen
# import random

# dej = Turtle()
# dej.shape("turtle")
# dej.color("red")
# colors = ["red","blue","green","pink","brown","orange"]
# count = 3
# while count  < 11:   
#     for n in range(count):
#         dej.forward(100)
#         dej.right(360/count)
#     rand_color = random.choice(colors)
#     dej.pencolor(rand_color)
#     count += 1

# dejo_house = Screen()
# dejo_house.exitonclick()

""" TURTLE RANDOM MOVEMENTS """
# from turtle import Turtle, Screen
# import random

# dej = Turtle()
# dej.shape("turtle")
# dej.pensize(10)

# def move_forward():
#     dej.forward(random.randint(1, 100))

# def move_left():
#     dej.left(90)

# def move_right():
#     dej.right(90)

# movement = [move_forward, move_left, move_right]

# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     dej.pencolor(r, g, b)

# screen = Screen()
# screen.colormode(255)  

# def random_movement():
#     rand_movement = random.choice(movement)
#     rand_movement()  
#     change_color()   
#     screen.ontimer(random_movement, 100)  

# random_movement()  

# screen.exitonclick()


""" TURTLE SPIROGRAPH """
# from turtle import Turtle, Screen, colormode
# import random

# circ_proj = Turtle()
# circ_proj.speed("fastest")
# colormode(255)


# def random_color():
#     r = random.randint(0,225)
#     g = random.randint(0,225)
#     b = random.randint(0,225)
#     color = (r, g, b)
#     return color

# def draw_spirograph(size):
#     for _ in range(int(720*5/size)):
#         circ_proj.color(random_color())
#         circ_proj.circle(100)
#         circ_proj.setheading(circ_proj.heading() + size)


# draw_spirograph(10)

# screen = Screen()
# screen.exitonclick()

""" TURTLE DOT ART """
# import colorgram
# import random 
# from turtle import Turtle, Screen, colormode
# import math

# colormode(255)
# turtle = Turtle()
# screen = Screen()
# turtle.shape("circle")
# turtle.speed(0)

# colors = colorgram.extract("20_001.jpg", 10)
# color = []
# for img in colors:
#     rgb = img.rgb
#     color.append((rgb.r, rgb.g, rgb.b))


# color.remove((229, 228, 226))
# color.remove((222, 224, 227))
# color.remove((225, 223, 224))
# print(color)
# time  = 36
# while time > 0:
#     time -= 1
#     for x in range(int(math.sqrt(time))):        
#         stamp_id = turtle.stamp()
#         turtle.penup()
#         turtle.forward(50)
#         turtle.pendown()
#         turtle.color(random.choice(color))
#     turtle.right(270)


# screen.exitonclick()
