THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

from tkinter import *

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window =Tk()
        self.window.title("Quizzler")
        
        self.window.config(bg=THEME_COLOR)
        self.window.config(pady=20, padx=20)
        self.score_label=Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.canvas=Canvas(width=300, height=250, bg='white')
        self.question_text= self.canvas.create_text(150, 125,width=280, text="Some Question", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)
        true_image=PhotoImage(file='./images/true.png')
        self.true_button=Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_image=PhotoImage(file='./images/false.png')
        self.false_button=Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    def true_pressed(self):
        is_right=self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def false_pressed(self):
        is_wrong=self.quiz.check_answer('False')
        self.give_feedback(is_wrong)
        
    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
# window=Tk()
# window.config(bg=THEME_COLOR)
# window.title("Quizzler")
# window.minsize(width=300, height=400)
# window.config(pady=20, padx=20)

# canvas=Canvas(width=250, height=250, bg="white")
# canvas.config(bg='white')
# canvas.grid(column=0, row=0, columnspan=2)


# true_button=Button(image='./images/true.png', highlightthickness=0, command=True)
# true_button.grid(column=0, row=1)
# false_button=Button(image='./images/false.png', highlightthickness=0, command=False)
# false_button.grid(column=1, row=1)

# window.mainloop()

