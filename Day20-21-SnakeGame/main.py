from turtle import Turtle, Screen
import time
screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
turtles=[]
screen.tracer(0)

def draw_three_turtle(x,y):
    for i in range(3):
        new_turtle=Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(x-i*20,y)
        turtles.append(new_turtle)

def move():
    screen.update()
    time.sleep(0.1)
    for i in range(2,0,-1):
        new_x=turtles[i-1].xcor()
        new_y=turtles[i-1].ycor()
        turtles[i].goto(new_x,new_y)
    turtles[0].forward(20)
    turtles[0].right(90)




draw_three_turtle(0,0)
screen.update()

game_on=True
while game_on:
    move()




screen.exitonclick()
