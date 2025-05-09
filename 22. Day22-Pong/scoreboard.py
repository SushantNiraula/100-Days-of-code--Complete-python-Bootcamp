from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))

    def leftscore(self):
        self.left_score += 1
        self.update_scoreboard()
    def rightscore(self):
        self.right_score += 1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Final scores are: {self.left_score} - {self.right_score}", align='center', font=('Courier', 80, 'normal'))
        self.write("Game Over", align='center', font=('Courier', 80, 'normal'))
