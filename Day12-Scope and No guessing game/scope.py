## Scope is the region of the program where a variable is defined and can be accessed.

enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies in function: {enemies}")
increase_enemies()
print(f'enemies outside function: {enemies}')
## here the enemies=2 inside the function increase_enemies is local(creates a new variable) to the function i.e it is only accessible within the function
# enemies=1 is global to the program i.e it is accessible from anywhere in the program

def decrease_enemies():
    global enemies ## we are using the global keyword to access the global variable enemies
    enemies+=2
    print(f"decrease enemies in function: {enemies}")
decrease_enemies()
print(f'decrease enemies outside function: {enemies}')

# other way is to pass the variable as an argument to the function
def change_enemies(enemies):
    enemies+=5
    print(f"change enemies in function: {enemies}")
    return enemies
enemies=change_enemies(enemies)
print(f'change enemies outside function: {enemies}')
