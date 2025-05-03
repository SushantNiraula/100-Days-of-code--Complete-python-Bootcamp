from turtle import Turtle, Screen
import random
from generate_random_RGB import random_color

timmy = Turtle()  
size_of_gap=5
timmy.speed('fastest')  
for i in range(int(360/size_of_gap)):
    r, g, b = random_color()
    timmy.color(r/255, g/255, b/255)
    timmy.circle(100)
    current=timmy.heading()
    timmy.setheading(current+size_of_gap)


screen=Screen()
screen.exitonclick()