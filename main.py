from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECKMARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    start_button.config(state="normal")
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_count():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        top_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_seconds)
        top_label.config(text="Break", fg=PINK)

    else:
        count_down(work_seconds)
        top_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    start_button.config(state="disabled")

    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        start_count()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += CHECKMARK
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(106, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

top_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
top_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_button = Button(text="Start",borderwidth=0.2, bg="white", command=start_count)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",borderwidth=0.2, bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)






window.mainloop()