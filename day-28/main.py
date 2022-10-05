import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
is_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(is_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    SHORT_BREAK = SHORT_BREAK_MIN * 60
    LONG_BREAK = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(LONG_BREAK)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
    else:
        count_down(SHORT_BREAK)
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = count // 60
    second = count % 60
    if second < 10:
        # second = "0" + str(second)
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global is_timer
        is_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = reps // 2
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


check_mark = tkinter.Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)


start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)
reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)


window.mainloop()
