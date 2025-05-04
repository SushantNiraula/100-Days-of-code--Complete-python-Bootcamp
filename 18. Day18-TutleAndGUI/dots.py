# import colorgram
# rgb_colors=[]
# colors=colorgram.extract('image.jpeg', 26)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
colors_list=[(211, 210, 210), (189, 167, 121), (57, 91, 111), (113, 43, 35),
              (210, 211, 214), (164, 89, 64), (207, 211, 208), (211, 209, 210),
                (171, 183, 169), (137, 150, 68), (64, 43, 43), (127, 160, 172), (101, 79, 89),
                (82, 133, 108), (108, 39, 44), (39, 62, 47), (45, 40, 41), (211, 196, 123), (174, 150, 152),
                  (36, 71, 88), (179, 105, 80), (35, 68, 84), (99, 142, 114), (206, 185, 181), (183, 199, 180)]

import random
from turtle import Turtle, Screen
timmy=Turtle()
# timmy.ht()

timmy.setheading(135)
timmy.penup()
timmy.forward(400)
timmy.setheading(0)
for i in range(10):
    for j in range(10):
        timmy.pendown()
        r,g,b=random.choice(colors_list)
        timmy.dot(20,(r/255,g/255,b/255))
        timmy.penup()
        timmy.forward(60)
    timmy.setheading(270)
    timmy.forward(60)
    timmy.setheading(180)
    timmy.forward(600)
    timmy.setheading(0)




screen=Screen()
screen.colormode(255)
screen.exitonclick()
