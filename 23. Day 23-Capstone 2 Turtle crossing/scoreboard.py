from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-240,270)
        self.score = 0
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT )

    def level_up(self):
        self.score += 1
        self.update()
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



