## for Loop and range are used to iterate over a sequence of numbers or items in a collection.

for i in range(1,101): # range(start, stop) generates numbers from start to stop-1 i.e 1 to 100
    print(i) # prints numbers from 1 to 100
# The range function can also take a third argument, which is the step size.
print(f"\nUsing range() with a step size of 2 to print even numbers from 0 to 10:")
for i in range(0, 11, 2): # range(start, stop, step) generates numbers from start to stop-1 with a step size of 2
    print(i) # prints even numbers from 0 to 10