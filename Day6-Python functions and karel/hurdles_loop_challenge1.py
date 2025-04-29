##  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

## go to link and click on "Run" to see the code in action
## we are going to use functions to make the code more readable and reusable
## turn_right is a function which turns the robot right
## overcome_hurdle is a function which makes the robot overcome the hurdle
## we are using conditionals to check if the front is clear or not and also while loop with condition that it runs until the robot reaches the goal
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

for i in range(6):
    move()
    overcome_hurdle()