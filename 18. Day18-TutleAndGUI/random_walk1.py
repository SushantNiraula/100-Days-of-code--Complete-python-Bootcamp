from turtle import Turtle, Screen
import random
from generate_random_RGB import random_color

timmy=Turtle()
directions=[0,90,180,270]

for i in range(200):
    r,g,b=random_color()
    timmy.color(r/255,g/255,b/255)
    timmy.pensize(15)
    timmy.speed(4)
    timmy.forward(20)
    timmy.setheading(random.choice(directions))
screen=Screen()
screen.exitonclick()