from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 0.5
reps=0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min= count // 60
    count_sec= count % 60

    canvas.itemconfig(timer_text,text=f'{count_min:02}:{count_sec:02}')
    if count>0:
        window.after(1000, count_down,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)
## Timer label
timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME, 40, "bold"),bg=YELLOW,padx=10,pady=10)
timer_label.grid(column=1,row=0)

## start and reset button
start_button =Button(text='Start',padx=5,pady=5,border=0,highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button =Button(text='Reset',padx=5,pady=5,border=0,highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

## check mark label
check_mark_label=Label(text="✔",fg=GREEN,font=(FONT_NAME, 40, "bold"),bg=YELLOW,padx=10,pady=10)
check_mark_label.grid(column=1,row=3)

canvas=Canvas(width=200, height=224 ,bg=YELLOW, highlightthickness=0)
tomato_img= PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row =1)



window.mainloop()