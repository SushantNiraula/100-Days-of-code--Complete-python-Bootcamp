## Here we will learn about function parameters and how to use them in Python.

def greet(name):
    """
    This function takes a name as a parameter and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}!")

# Example usage
greet("Alice")  # Output: Hello, Alice!
def add_numbers(a, b):
    """
    This function takes two numbers as parameters and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b
# Example usage 
result = add_numbers(5, 10)  # result will be 15
print(result)  # Output: 15
## until now we have learned about function parameters and how to use them in Python.
# And we used positional parameters in the above examples.
# Now we will learn about keyword parameters.
def greet(name="World"):
    """
    This function takes a name as a parameter and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet. Default is "World".
    
    Returns:
    None
    """
    print(f"Hello, {name}!")
# Example usage
greet()  # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
# In the above example, we have used a default parameter.
# Now we will learn about keyword parameters.
def greet(name, age):
    """
    This function takes a name and age as parameters and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet.
    age (int): The age of the person to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}! You are {age} years old.")
# Example usage 
greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.
greet(age=25, name="Alice")  # Output: Hello, Alice! You are 25 years old.
# In the above example, we have used keyword parameters.
