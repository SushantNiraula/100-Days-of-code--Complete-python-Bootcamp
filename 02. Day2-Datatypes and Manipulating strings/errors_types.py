## we are going to define the errors types in python 

try:
    print(len(10)) # TypeError: object of type 'int' has no len()
except TypeError as e:
    print(f"TypeError: {e}")

## Other common error is NameError
try:
    print(undeclared_variable) # NameError: name 'undeclared_variable' is not defined
except NameError as e:
    print(f"NameError: {e}")
## Other common error is SyntaxError

#3 but cannnot show the syntax error as it is a syntax error where the code is not valid to even run

## Other common error is IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[3]) # IndexError: list index out of range
except IndexError as e:
    print(f"IndexError: {e}")
## Other common error is KeyError
try:
    my_dict = {"name": "John"}
    print(my_dict["age"]) # KeyError: 'age'
except KeyError as e:
    print(f"KeyError: {e}")
## Other common error is AttributeError
try:
    my_string = "Hello"
    print(my_string.non_existent_method()) # AttributeError: 'str' object has no attribute 'non_existent_method'
except AttributeError as e:
    print(f"AttributeError: {e}")
## Other common error is ValueError
try:
    int("abc") # ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(f"ValueError: {e}")
## Other common error is ZeroDivisionError
try:
    print(1 / 0) # ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
