import tkinter
from gotify import Gotify
from pathlib import Path
import credentials
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#FD8D14"
TOMATO_RED_LIGHT = "#f26849"
TOMATO_RED_DARK = "#f1583f"
RED = "#FF6868"
TOMATO_GREEN = "#379b46"
GREEN = "#71d33c"
YELLOW = "#FFE17B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
current_state = "Timer"

started = False
reps = 0
reset = False


p = Path(__file__).with_name('tomato.png')
tomato_path = p.absolute()
# ---------------------------- GOTIFY SETUP ------------------------------- # v
gotify_url = credentials.gotify['url']
gotify_token = credentials.gotify['token']

gotify = Gotify(base_url=gotify_url,
                app_token=gotify_token)
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global started
    global reps
    global reset
    if started:
        window.after_cancel(timer)
        if reps > 0:
            reps -= 1
        started = False
        canvas.itemconfig(timer_text, text="00:00")
        color_stuff(ORANGE)
        reset = True
    elif not reset:
        reset = True
        if reps >= 0:
            reps -= 1
        color_stuff(ORANGE)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global started
    global reps
    global reset
    global current_state
    reset = False
    if not started:
        reps += 1
        if reps % 2 != 0:
            count_down(WORK_MIN*60)
            current_state = "Work"
            color_stuff(YELLOW)
        elif reps == 8:
            count_down(LONG_BREAK_MIN * 60)
            current_state = "Long Break"
            color_stuff(GREEN)
            reps = 0
        else:
            count_down(SHORT_BREAK_MIN * 60)
            current_state = "Short Break"
            color_stuff(GREEN)

        timer_label.config(text=current_state)
        checkmark_number = int(reps / 2)
        checkmark.config(text=(checkmark_number * "✔"))
        started = True



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds_to_count_down):
    global started
    global current_state
    if seconds_to_count_down > 0:
        global timer
        timer = window.after(1000, count_down, seconds_to_count_down -1)
    else:
        started = False
        window.focus_force()
        gotify.create_message(
            current_state + " finished",
            title="Pomodoro",
            priority=0,
        )
    minutes_int = int(seconds_to_count_down / 60)
    seconds_int = int(seconds_to_count_down % 60)
    # add 0 in front if only one number
    minutes = str(minutes_int).zfill(2)
    seconds = str(seconds_int).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(text="Timer", fg=TOMATO_GREEN, bg=YELLOW, font=(FONT_NAME,35,"bold"), width=12)
start_button = tkinter.Button(text="Start", command=start_timer, bg=YELLOW, activebackground=TOMATO_RED_DARK,
                              highlightthickness=0)
reset_button = tkinter.Button(text="Reset", command=reset_timer, bg=YELLOW, activebackground=TOMATO_RED_DARK,
                              highlightthickness=0)
checkmark = tkinter.Label(text="", fg=TOMATO_GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
tomato_img = tkinter.PhotoImage(file=tomato_path)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME,35,"bold"))

timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
checkmark.grid(column=1, row=3)


# ---------------------------- COLOR CHANGES ------------------------------- #
def color_stuff(main_color):
    for element in [timer_label, checkmark, window, canvas, start_button, reset_button]:
        element.config(bg=main_color)




window.mainloop()
