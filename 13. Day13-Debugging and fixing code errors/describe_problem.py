# Day13-Debugging and fixing code errors/describe_problem.py
# Here we are going to describe the problem we are trying to solve. it is an important part of the learning process.
def my_function():
    for i in range(0,20):
        if i==20:
            print("You got it")

my_function()
## here the problem is that the range is from 0 to 20, so the loop will never reach 20
## to fix this, we can change the range to 0 to 21
## This is therefore bug in Understanding the problem. You must be able to describe the problem to be able to fix it

# Describe the problem
# Write your answers as comments.
# 1. What is the for loop doing?
# 2. When is the function meant to print you got is?
# 3. What are the assumptions about the value of i?
