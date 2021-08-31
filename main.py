from tkinter import *
import math

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    text.config(text="Timer", fg=GREEN)
    canv.itemconfig(canv_timer, text="00:00")
    checkbox.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        minutes = LONG_BREAK_MIN
        text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        minutes = SHORT_BREAK_MIN
        text.config(text="Break", fg=PINK)
    else:
        minutes = WORK_MIN
        text.config(text="Work", fg=GREEN)
    count_down(minutes * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canv.itemconfig(canv_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_times = math.floor(reps / 2)
        for _ in range(work_times):
            marks += "✔"
        checkbox.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# ---------------------------- CANVAS ------------------------------- #
canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canv.create_image(100, 112, image=tomato_img)
canv_timer = canv.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canv.grid(column=1, row=1)
# ---------------------------- BUTTONS ------------------------------- #
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)
# ---------------------------- TEXT ------------------------------- #
text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), highlightthickness=0, bg=YELLOW)
text.grid(column=1, row=0)
checkbox = Label(fg=GREEN, highlightthickness=0, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
checkbox.grid(column=1, row=3)

window.mainloop()
