from turtle import Turtle
class Player(Turtle):
    def __init__(self,player_id):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle(player_id)
    def paddle(self,player):
        if player==1:
            self.goto(350,0)
        elif player==2:
            self.goto(-350,0)
    def up(self):
        if self.ycor()<240:
            self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        if self.ycor()> -240:
            self.goto(self.xcor(),self.ycor()-20)
