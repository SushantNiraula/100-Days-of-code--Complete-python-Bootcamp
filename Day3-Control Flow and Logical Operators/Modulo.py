'''
Modulo is a mathematical operation that returns the remainder of a division.
for example, 5 % 2 = 1 because when you divide 5 by 2, the remainder is 1.
Modulo is often used in programming to determine if a number is even or odd.
'''
# Example 1: Check if a number is even or odd
number = int(input("Enter a number you want to check if it is even or odd: "))
if number % 2== 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# Example 2: Check if a number is divisible by 3
number = int(input("Enter a number you want to check if it is divisible by 3: "))

if number % 3 == 0: ## this checks if the remainder of the division of number by 3 is 0
    print(f"{number} is divisible by 3 ✅")
else:
    print(f"{number} is not divisible by 3 ❌") #can be used to check if a number is divisible by any number

