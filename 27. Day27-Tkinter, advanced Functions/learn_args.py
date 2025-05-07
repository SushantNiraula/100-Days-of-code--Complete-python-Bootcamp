
def add(*args):
    sum=0
    # args is tuple of all the arguments passed when calling the function.
    for n in args:
        sum+=n
    return sum

sum=add (3,4,5,6,7,8,10)
print(sum)

