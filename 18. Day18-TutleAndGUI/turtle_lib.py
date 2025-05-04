from turtle import Turtle,Screen
timmy=Turtle()

timmy.shape("turtle")
timmy.color("red")

## Drawing a square using turtle timmy
for i in range(4):
    timmy.forward(100)
    timmy.left(90)
# Drawing a dashed line
for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    


















screen=Screen()
screen.exitonclick()



