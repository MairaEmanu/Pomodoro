from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BACKGROUND = "#fef9d9"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    # stop the loop for the timer
    window.after_cancel(timer)
    # Reset the timer text + title label
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=BACKGROUND)

    #reset all the variables needed for the worksessions
    global reps
    reps = 0
    check_marks.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60


    # Adjust to the right time format:
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions =  math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BACKGROUND)





#Background canvas
canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# widgets
button_start = Button(text="Start", command=start_timer, highlightbackground=BACKGROUND, padx=10)
button_start.grid(row=2, column=0, sticky="w")
button_reset = Button(text="Reset", highlightbackground=BACKGROUND, padx=10, command=timer_reset)
button_reset.grid(row=2, column=2, sticky="w")

check_marks = Label(font=(FONT_NAME,30),bg=BACKGROUND, fg=GREEN)
check_marks.grid(column=1, row=3)

label_timer = Label(text="Timer", font=(FONT_NAME,50),fg=GREEN, bg=BACKGROUND)
label_timer.grid(row=0, column=1, sticky="n")





window.mainloop()


