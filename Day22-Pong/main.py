from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.tracer(0)
tim=Turtle(shape='square')
## Creating Players
player1=Player(1)
player2=Player(2)
ball=Ball()
score=Scoreboard()
## Setting Screens
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title('Pong')

## Paddle listening and click reponse
screen.listen()
screen.onkey(player1.up,key="Up")
screen.onkey(player1.down,key='Down')
screen.onkey(player2.up,key='w')
screen.onkey(player2.down,key='s')

game_on=True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    print(ball.distance(player1))
    ## collision with the wall
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.bounceback()

    ## detect collision with paddles
    if (ball.xcor()< -330 and ball.distance(player2)< 50) or (ball.xcor()> 330 and ball.distance(player1)< 50):
        ball.bounce_x()
    if ball.xcor()>380 :
        ball.reset_position()
        score.rightscore()
    if ball.xcor()< -380:
        ball.reset_position()
        score.leftscore()
    if score.leftscore ==5 or score.rightscore==5:
        score.game_over()
        game_on=False

screen.exitonclick()
