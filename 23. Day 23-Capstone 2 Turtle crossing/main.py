import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player1=Player()
scoreboard = Scoreboard()
car_manager=CarManager()
screen.onkey(player1.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()
    if player1.check_finish():
        player1.generate()
        scoreboard.level_up()
        car_manager.update_speed()
    for car in car_manager.cars:
        if car.distance(player1) < 20:
            scoreboard.game_over()
            game_is_on = False
    screen.update()


screen.exitonclick()