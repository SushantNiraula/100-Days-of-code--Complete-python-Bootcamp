'''
Loops are a fundamental concept in programming that allows you to automate repetitive tasks.
Instead of writing the same lines of code multiple times, you can use a loop to execute a block of code repeatedly.
Python offers two main types of loops: for loops and while loops.


'''
fruits=['apple','banana','mango','pineapple','litchi']
## Imagine you have a list of your favorite fruits 
# If you wanted to print each fruit, you could do it like this:
print(f"Manually printing each fruit:")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

'''
But what if you had 100 fruits? That would be a lot of typing!
 This is where for loops come in handy. A for loop allows you to iterate over each item in a sequence
 (like a list, string, or tuple) and perform an action on each item.
 '''
print(f"\nUsing a for loop to print each fruit:")
for fruit in fruits:
    print(fruit)

'''
Another common way to use for loops is with the range() function. range() creates a sequence of numbers.
 For example, range(5) generates the sequence 0, 1, 2, 3, 4.
 You can use this to repeat an action a specific number of times:
'''
print(f"\nUsing range() to print numbers from 0 to 4:")
for i in range(5):
    print(i)
