'''

try: Something that might cause an exception

except: Do this if there was an exeption

else: Do this if there was no exception i.e no error

finally: Do this no matter what happens

'''
try: 
    with open('test.txt','r') as f:
        print(f.read())

except FileNotFoundError as error_message:
    print("File not found error")
    with open('test.txt','w') as f:
        f.write("This is a test file")
    print("File created")
else:
    print("File found")
    
finally:
    print("This will always run")
    # f.close() ## not needed as we are using with open
    
try:
    x=10/0
except ZeroDivisionError as error_message:
    print("You cannot divide by zero")
    print(error_message)
else:
    print("No error")
finally:
    print("This will always run")