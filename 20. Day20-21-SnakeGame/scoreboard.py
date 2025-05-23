from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        with open("highscore.txt") as f:
            self.highscore = int(f.read())
            f.close()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over Your score is {self.score}", align="center", font=("Courier", 24, "normal")) # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over Your score is {self.score}", align="center", font=("Courier", 24, "normal"))
    def reset(self):
        if self.score> self.highscore:
            self.highscore = self.score
            with open("highscore.txt",'w') as f:
                f.write(str(self.highscore))
        self.score=0
        self.update_scoreboard()