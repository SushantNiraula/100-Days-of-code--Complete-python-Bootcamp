from turtle import Turtle, Screen
import random

colors = ['slate gray', 'orange red', 'midnight blue', 'steel blue', 
          'light sea green', 'dark green', 'dark red', 'red', 
          'dark slate blue', 'dark violet']

timmy = Turtle()
timmy.shape("turtle")
pen_width = 15
timmy.pensize(pen_width)
timmy.speed(4)

def random_walk(rand_move):
    if rand_move == 0:
        timmy.forward(20)   
    elif rand_move == 1:
        timmy.right(90)
        timmy.forward(20)
    elif rand_move == 2:
        timmy.left(90)
        timmy.forward(20)
    elif rand_move == 3:
        timmy.backward(20)

screen = Screen()

while True:
    random_color = random.choice(colors)
    timmy.color(random_color)
    random_move = random.randint(0, 3)
    random_walk(random_move)

# Keep the screen open until clicked
screen.exitonclick()
