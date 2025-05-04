## In this challenge don't know where the hudddles is and even how high the hurdle is.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def ascend():
    turn_left()
    move()
    turn_right()
    if front_is_clear():
        descend()
    
def descend():
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        ascend()

## Lecture's version.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()