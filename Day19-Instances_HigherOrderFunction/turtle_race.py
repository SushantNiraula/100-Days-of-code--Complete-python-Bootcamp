from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
colors=['blue','red','yellow','pink','purple']
turtles=[]
user_bet=screen.textinput(title="Make a bet",prompt="Make a bet which color turtle would win: blue, red, yellow, pink, purple")
y_positions=[-80,-40,0,40,80]
for i in range(5):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_positions[i])
    turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"Your turtle {user_bet} won!")
                turtle.write("Race ends")
            else:
                print(f"You lost: {winner} won the race!")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
