import turtle
import pandas as pd
screen= turtle.Screen()
screen.title("U.S. States Game")
image='./blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv('./50_states.csv')
all_states=data['state'].to_list()
guessed_states=[]
score=0
game_on=True
screen.tracer(0)
while game_on:
    
    answer_state=screen.textinput(title=f'{score}/50 Guess the State',prompt='What\'s another state\'s name?')
    if answer_state == None:
        game_on=False
    if answer_state.title() in all_states:
        guessed_states.append(answer_state.title())
        state_data=data[data['state']==answer_state.title()]
    
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data.x.item()),int(state_data.y.item()))
        t.write(answer_state,align='center',font=('Arial',10,'normal'))
        score+=1
    if score == 50:
        game_on=False
        print('You guessed all the states')
    
    screen.update()






def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


