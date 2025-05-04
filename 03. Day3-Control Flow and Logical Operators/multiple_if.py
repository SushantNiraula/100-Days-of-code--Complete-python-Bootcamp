'''
Multiple if statements are used when you want to check multiple conditions independently
i.e. if one condition is true, it will execute the code block for that condition and then check the next condition.

the difference between if-else and multiple if statements is that in if-else, only one block of code will be executed
if-else syntax:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
elif condition3:
    # code to execute if condition3 is true
else:
    # code to execute if none of the conditions are true

multiple if syntax:
if condition1:
    # code to execute if condition1 is true
if condition2:
    # code to execute if condition2 is true
if condition3:
    # code to execute if condition3 is true

in if-else only one block of code will be executed but in multiple if statements, all the blocks of code will be executed
'''
# we use the same ticketing example to demonstrate multiple if statements
print("Welcome to the roller coaster!")
bill=0.0
height = int(input(" What is your height in cm?"))

if height > 120:
    print("You can ride the roller coaster!")
    age= int (input("What is your age?"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3
        # i.e if photo is taken, add $3 to the bill
    
    print(f"Your final bill is ${bill}.")

else:
    print("You cannot ride the roller coaster!")
