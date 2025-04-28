## Here we will create a program that simulates a pizza delivery service.

print("Welcome to the Pizza Delivery Service!")
size= input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
'''
## The cost of the pizza is as follows:
Small pizza costs $15
Medium pizza costs $20
Large pizza costs $25

Pepperoni for small pizza costs $2
Pepperoni for medium and large pizza costs $3
Extra cheese for any size pizza costs $1

'''
bill=0 # initialize bill to 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill +=3
    if extra_cheese == "Y":
        bill += 1
else:
    print("Invalid size. Please enter S, M, or L.")
    exit()
print(f"Your final bill is ${bill}.")