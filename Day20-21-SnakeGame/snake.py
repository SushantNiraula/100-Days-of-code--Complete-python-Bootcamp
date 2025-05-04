from turtle import Turtle, down
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.segments=[] # it holds the small segments of snake we create.
        self.create_snake()

    def create_snake(self):
        m=3
        for i in range(m):
            self.add_segment((i*(-20),0))

    def add_segment(self,position):
        tim=Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def move_snake(self):
        for i in range(len(self.segments)-1,0,-1):
            prev_xcor=self.segments[i-1].xcor()
            prev_ycor=self.segments[i-1].ycor()
            self.segments[i].goto(prev_xcor,prev_ycor)

        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading()!=down:
            self.segments[0].setheading(up)

    def down(self):
        if self.segments[0].heading()!=up:
            self.segments[0].setheading(down)

    def left(self):
        if self.segments[0].heading()!=right:
            self.segments[0].setheading(left)

    def right(self):
        if self.segments[0].heading()!=left:
            self.segments[0].setheading(right)
    def extend(self):
        pos=self.segments[-1].position()
        self.add_segment(pos)
