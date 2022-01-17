from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#66DE93"
L_PINK = "FFD8CC"
PEACH = "#FFEEDB"
WHITE = "#F9F9F9"
TOMATO = "#DF5E5E"
D_PINK = "#FFBD9B"
mark = ""

FONT_NAME = "Amithen"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS
    global mark
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Pomodoro Timer", fg=D_PINK)
    REPS = 0
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    global mark
    REPS += 1
    print(REPS)
    l_b = LONG_BREAK_MIN * 60
    s_b = SHORT_BREAK_MIN * 60
    w_s = WORK_MIN * 60
    if REPS % 8 == 0:
        timer.config(text="Break for 20 Mins!!", fg=RED)
        count_down(l_b)
        return
    elif REPS % 2 == 0:
        timer.config(text="Break for 5 Mins!!", fg=PINK)
        count_down(s_b)
        mark += "✔"
        checkmark.config(text=mark)
    else:
        timer.config(text="Work time!!")
        count_down(w_s)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS
    i_minute = math.floor(count / 60)
    i_second = count % 60
    minute = i_minute
    second = i_second
    if i_minute < 10:
            minute = f"0{i_minute}"
    if i_second < 10:
            second = f"0{i_second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if i_minute == 0 and i_second == 0:
        start_timer()
    elif i_second == 0:
        i_minute -= 1
        i_second = 59
    else:
        i_second -= 1
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.config(padx=40, pady=20)
window.title("Pomorodo")
window.config(bg=PEACH)

canvas = Canvas(width=250, height=250, bg=PEACH, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)

timer_text = canvas.create_text(130, 140, text="00:00", fill="white", font=("Mv boli", 30, "bold"))

canvas.grid(column=1, row=1)

timer = Label(text="Pomodoro Timer", font=(FONT_NAME, 30, "bold"), bg=PEACH, fg=D_PINK)
timer.grid(column=1, row=0)

start_button = Button(text="  Start  ", font=(FONT_NAME, 20, "bold"), bg=D_PINK, fg=WHITE, borderwidth=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="  Reset  ", font=(FONT_NAME, 20, "bold"), bg=D_PINK, fg=WHITE, borderwidth=0,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(text=mark, bg=PEACH, fg=GREEN, font=("Arial", 20, "normal"))
checkmark.grid(column=1, row=3)

check_button = Checkbutton()

window.mainloop()
