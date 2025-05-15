## Python decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
## Ability to treat functions as first-class objects and can be passed around as arguments, returned from other functions, and assigned to variables.
#  
# def calculate(calc_FUNCTION,a, b):
#     return calc_FUNCTION(a, b)
# result= calculate(lambda x, y: x+y, 5, 10)
# print(result)

# def outer_func():
#     print("Outer function")
#     def inner_func():
#         print("Inner function")
#         ##because inner function is defined inside outer function, is can only be called inside outer function

# def outer_func():
#     print("Outer function")
#     def inner_func():
#         print("Inner function")

#     return inner_func

# inner_function=outer_func()
# inner_function()
import time 


## decorator function helps us to extend the behavior of the original function without modifying it.
def delay_decorator(original_funtion):
    
    def wrapper_function():
        time.sleep(2)
        original_funtion()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello, World!")

say_hello()
## decorator function helps us to extend the behavior of the original function without modifying it.