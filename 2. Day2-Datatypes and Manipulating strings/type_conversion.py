## Let's use type conversion to convert a string to an integer
string_number="123"
print(f'The string_number is {string_number} and has type {type(string_number)}') # string_number is a string
int_number=int(string_number) # convert string to int
print(f'The int_number is {int_number} and has type {type(int_number)}') # int_number is an integer

bool=True
print(f'The bool is {bool} and has type {type(bool)}') # bool is a boolean
int_number=int(bool) # convert bool to int
print(f'The int_number is {int_number} and has type {type(int_number)}') # int_number is an integer
float_number=float(bool) # convert bool to float
print(f'The float_number is {float_number} and has type {type(float_number)}') # float_number is a float

# But we cannot convert a int,float and strings to bool

