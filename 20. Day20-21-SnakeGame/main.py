from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)
game=Snake()
food=Food()
scoreboard=Scoreboard()
screen.update()
is_game_on=True
screen.listen()
screen.onkey(key="w",fun=game.up)
screen.onkey(key="s",fun=game.down)
screen.onkey(key='a',fun=game.left)
screen.onkey(key='d',fun=game.right)
while is_game_on:
    screen.update()
    time.sleep(0.1)
    game.move_snake()

    # Detect  collision with food
    if game.segments[0].distance(food)<15:
        food.refresh()
        game.extend()
        scoreboard.increase_score()
    ## detect boundary crossing
    if game.segments[0].xcor()>280 or game.segments[0].ycor()>280 \
        or game.segments[0].xcor()< -280 or game.segments[0].ycor() < -280:
        scoreboard.game_over()
        is_game_on=False

    ## detect collision with tail
    for segment in game.segments[1:]:
        if game.segments[0].distance(segment) <10:
            scoreboard.game_over()
            is_game_on=False



screen.exitonclick()
