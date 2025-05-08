from tkinter import *
from tkinter import messagebox
import pyperclip
import json
##---------------------------------- Password Generator ------------------------------- #
import random
## pypassword generator 
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','?','/']

def generate_password():
    password_entry.delete(0,END)
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,5)
    nr_numbers = random.randint(2,5)

## Hard Level
    password_list=[]
    rn_letters=[random.choice(letters) for _ in range(0,nr_letters-1)]
    rn_symbols=[random.choice(symbols) for _ in range(0,nr_symbols-1)]
    rn_numbers=[random.choice(numbers) for _ in range(0,nr_numbers-1)]
    password_list.extend(rn_letters)
    password_list.extend(rn_symbols)
    password_list.extend(rn_numbers)
    random.shuffle(password_list)
    # password=""
    # for word in password_list:
    #     password+=word
    password="".join(password_list)
    pyperclip.copy(password) ## this copies the password to clipboard
    password_entry.insert(0,password)


### ---------------------------- SAVE Password ------------------------------- #

def add_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            'email':email,
            'password':password
        }
    }
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Error", message="Please fill in all fields")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open('user_data.json','r') as file:
                    data=json.load(file)
                    
            except FileNotFoundError:
                with open('user_data.json','w') as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open('user_data.json','w') as file:
                    json.dump(data,file,indent=4)
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)
                    email_entry.delete(0,END)
                    email_entry.insert(0,"example@gmail.com")
                    website_entry.focus()
            

            messagebox.showinfo(title="Success", message="Password saved successfully!")

    ## Dialog box pop up 

## -------------------------------------UI------------------------------------- ##
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=400, height=400)
window.config(bg="white")
canvas=Canvas(width=200, height=200, bg="White",highlightbackground="white")

logo_img=PhotoImage(file='../29. Day29-Password Manager/logo.png')
canvas.create_image(125, 125, image=logo_img, anchor=CENTER)
canvas.grid(column=1, row=0)


website_label=Label(text="Website:", bg="white",fg="black", font=("Arial", 20, "bold"))
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)
website_entry=Entry(width=35,bg="white",fg="black", font=("Arial", 20, "bold"))
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus()

## Email/Username
email_label=Label(text="Email/Username:", bg="white",fg="black", font=("Arial", 20, "bold"))
email_label.grid(column=0, row=2)
email_label.config(padx=5, pady=5)
email_entry=Entry(width=35,bg="white",fg="black", font=("Arial", 20, "bold"))
email_entry.insert(0,"example@gmail.com")
email_entry.grid(column=1, row=2,columnspan=2)


## Password
password_label=Label(text="Password:", bg="white",fg="black", font=("Arial", 20, "bold"))
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)
password_entry=Entry(width=21,bg="white",fg="black", font=("Arial", 20, "bold"))
password_entry.grid(column=1, row=3)


## Generate Password button
generate_password_button=Button(text="Generate Password",highlightthickness=0,bg='white',command=generate_password)
generate_password_button.grid(column=2, row=3)

## Add button

add_button=Button(text="Add",width=36,highlightthickness=0,bg='white',command=add_password)

add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()  