from turtle import Turtle, Screen
import random 
colors=['slate gray','orange red','midnight blue','steel blue','light sea green','dark green','dark red','red','dark slate blue','dark violet']

timmy=Turtle()
for i in range(3,10):
    random_color=random.choice(colors)
    timmy.color(random_color)
    for j in range(i):
        
        timmy.forward(100)
        timmy.right(360/i)






screen=Screen()
screen.exitonclick()