from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_speed=STARTING_MOVE_DISTANCE
        self.cars=[]
    def create_car(self):
        chance=random.randint(0,6)
        if chance==0:
            new = Turtle('square')
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.color(random.choice(COLORS))
            new.penup()
            random_y = random.randint(-250, 250)
            new.goto(300, random_y)
            self.cars.append(new)

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)
    def update_speed(self):
        self.move_speed += MOVE_INCREMENT

