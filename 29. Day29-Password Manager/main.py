from tkinter import *

window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=400, height=400)
window.config(bg="white")
canvas=Canvas(width=200, height=200, bg="White",highlightbackground="white")

logo_img=PhotoImage(file='./logo.png')
canvas.create_image(125, 125, image=logo_img, anchor=CENTER)
canvas.grid(column=1, row=0)

website_label=Label(text="Website:", bg="white",fg="black", font=("Arial", 20, "bold"))
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)
website_entry=Entry(width=20,bg="white",fg="black", font=("Arial", 20, "bold"))
website_entry.grid(column=1, row=1)
website_entry.focus()
window.mainloop()  