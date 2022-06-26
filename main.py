import tkinter
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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def starttimer():
    global reps
    reps+=1
    worksec=WORK_MIN*60
    shortbreaksec=SHORT_BREAK_MIN*60
    longbreaksec=LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(longbreaksec)
        label1.config(text="Break",fg=RED)
    elif reps%2==0:
        countdown(shortbreaksec)
        label1.config(text="Break", fg=PINK)

    else:
        countdown(worksec)
        label1.config(text="Working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    countmin=math.floor(count/60)
    countsec=count%60

    if countsec<10:
        countsec=f"0{countsec}"

    if countmin<10:
        countmin=f"0{countmin}"

    canvas.itemconfig(timer_text, text=f"{countmin}:{countsec}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        starttimer()
        mark=""
        for n in range(math.floor(reps/2)):
            mark+="✓"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = tkinter.Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
x = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=x)
timer_text =canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

label1=tkinter.Label(text="Timer",font=(FONT_NAME,35,"bold"),bg=YELLOW,foreground=GREEN)
label1.grid(column=1,row=0)

buttonstart=tkinter.Button(text="Start",command=starttimer)
buttonstart.grid(column=0,row=2)

buttonreset=tkinter.Button(text="Reset",command=reset_timer)
buttonreset.grid(column=2,row=2)

label2=tkinter.Label(text="",foreground=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
label2.grid(column=1,row=3)

window.mainloop()