"""
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false


"""

# Example 1: Check Bathtub Water Level
water_level =50
if water_level > 100:
    print("Drain the bathtub")
else:
    print("The bathtub is at a safe level")

## Example 2: Roller coaster ticketing

print("Welcome to the roller coaster!")
height=int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12: # this is nested if statement i.e if statement is nested inside another if statement 
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You cannot ride the roller coaster!")

""" All comparision operators are 
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
"""