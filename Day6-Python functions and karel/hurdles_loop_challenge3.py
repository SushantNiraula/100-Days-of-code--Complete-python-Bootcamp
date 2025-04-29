## In this case : 
## We don't know where the hurdle even is. 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def overcome_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        overcome_hurdle()

