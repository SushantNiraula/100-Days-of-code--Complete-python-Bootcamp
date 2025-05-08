## suppose we want the use to enter a number but rather if we want to enter a string we want to raise an exception

input_no=input("Enter a number: ")
try:
    if not input_no.isdigit():
        raise ValueError("Please enter a number")
    else:
        print("You entered a number")
except ValueError as error_message:
    print(error_message)