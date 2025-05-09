BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas as pd
data=pd.read_csv('./data/french_words.csv')

##-----------------Button functions-----------------##
def show_french_word():
    french_word=data.sample (1)
    french_word=french_word['French'].values[0]
    english_word=data[data['French']==french_word]['English'].values[0]
    canvas.itemconfig(3,text=french_word)



##-----------------UI-----------------##
window=Tk()
window.config(padx=50,pady=50)
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526)
image_path=PhotoImage(file='./images/card_front.png')
canvas.create_image(400,263,image=image_path)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
canvas.create_text(400,150,text="French",font=("Arial",40,"italic"),fill="black")
canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"),fill="black")

cross_image=PhotoImage(file='./images/wrong.png')
unknown_button=Button(image=cross_image,highlightthickness=0,command=show_french_word)   
unknown_button.grid(row=1,column=0)
tick_image=PhotoImage(file='./images/right.png')
yes_button=Button(image=tick_image,highlightthickness=0,command=show_french_word)
yes_button.grid(row=1,column=1)




window.mainloop()