# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
## In this case we don't know where the final goal is
## we are going to use functions to make the code more readable and reusable
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