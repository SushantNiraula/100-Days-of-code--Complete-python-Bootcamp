import random
## pypassword generator 
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','?','/']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password=""
## Easy Level 
for i in range(0,nr_letters):
    rn_letter=random.choice(letters)
    password+=rn_letter
for i in range(0,nr_symbols):
    rn_symbol=random.choice(symbols)
    password+=rn_symbol
for i in range(0,nr_numbers):
    rn_number=random.choice(numbers)
    password+=rn_number
print(f"Your password is: {password}")

## Hard Level
password_list=[]

for i in range(0,nr_letters):
    rn_letter=random.choice(letters)
    password_list.append(rn_letter)
for i in range(0,nr_symbols):
    rn_symbol=random.choice(symbols)
    password_list.append(rn_symbol)
for i in range(0,nr_numbers):
    rn_number=random.choice(numbers)
    password_list.append(rn_number)
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for word in password_list:
    password+=word

print("The password is : ",password)