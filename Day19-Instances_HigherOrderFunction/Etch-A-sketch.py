from turtle import Turtle, Screen
import random

timmy=Turtle()
def move_forward():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def clockwise():
    timmy.setheading(timmy.heading()+10)
def counter_clockwise():
    timmy.setheading(timmy.heading()-10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
def move_without_pen():
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
screen=Screen()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="c",fun=clear_screen)
screen.onkey(key="x",fun=move_without_pen)

screen.exitonclick()
