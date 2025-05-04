def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

functions={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
# Multiply the first number by the second number using dictionary

# print(functions['*'](2,3))
num1=float(input('Enter the first number: '))

continue_=True
while continue_==True:
    for symbol in functions:
        print(symbol)
    operation= input('Entert operation: ')
    num2=float(input('Enter the second number: '))  
    answer=functions[operation](num1,num2)
    print(f'{num1} {operation} {num2} = {answer}')
    choice=input(f'Do you want to continue with the  {answer} as first input (y/n): ').lower()
    if choice=='y':
        continue_=True
        num1=answer
    else:
        continue_=False