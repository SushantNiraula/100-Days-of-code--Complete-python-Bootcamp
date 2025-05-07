from tkinter import *
window= Tk()
window.title("My first GUI")
window.minsize(500,300)






## Label
my_label = Label(text="I Am a Label",font=("Arial",24,'bold'))
# my_label.pack() ## TO show label or any thing into screen we must pack it
my_label['text']='New Text'
my_label.config(text='New Text')
my_label.grid(column=0, row=0)
def button_clicked():
    my_label.config(text=user_input.get())
## Button
button = Button(text="Click Me",command=button_clicked)
# button.pack()
# button.place(x=100,y=100) ## so specific and coordinate should be fix. Very difficult to manage
button.grid(column=0, row=1)
## Entry
user_input=Entry(width=10)
user_input.grid(column=0,row=2)

# user_input.pack()












window.mainloop() ## It keeps the windows up until we manually close it.