# from turtle import Turtle, Screen
#
# tim = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('red')
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)



# 167
# import turtle
# tim = turtle.Turtle()
#
# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()


# from turtle import *
# from random import *
#
# choice([1, 2, 3])

# import heroes
# print(heroes.gen())


# 168
# import turtle as t
#
# tim = t.Turtle()
# tim.shape('turtle')
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()



# 169
# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.shape('turtle')
# colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
#
# def draw_shape(num_sides):
#     jason = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(jason)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)



# 170
# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.shape('turtle')
# colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed('fastest')
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



# 171
# import turtle as t
# import random
#
# tim = t.Turtle()
# tim.shape('turtle')
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed('fastest')
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



# 172
import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()