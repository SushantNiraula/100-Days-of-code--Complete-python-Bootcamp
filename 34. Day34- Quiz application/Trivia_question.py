from tkinter import *

window=Tk()
window.title('Trivia Quiz')
window.config(bg='white',padx=40,pady=40)
window.minsize(width=600, height=500)

canvas=Canvas(width=400, height=200)
canvas.config(bg='red')
canvas.grid(row=0, column=1)
canvas.create_image()


window.mainloop()