from tkinter import *
from datetime import date, datetime, time

bg = 'black'
fg = 'cyan'

app = Tk()
app.title('Age Calculator')
app.geometry('250x250')
app['background'] = bg


msg = Label(app, text='Enter your Date of Birth', background=bg, foreground=fg)
msg.grid(row=0, column=0,columnspan=3)

dayL = Label(app, text='Day:', background=bg, foreground=fg)
dayE = Entry(app, width=2)

monL = Label(app, text=' Month: ',background=bg, foreground=fg)
monE = Entry(app, width=2)

yrL = Label(app, text=' Year: ', background=bg, foreground=fg)
yrE = Entry(app, width=4)


dayL.grid(row=1, column=0)
dayE.grid(row=1,column=1)
monL.grid(row=1, column=2)
monE.grid(row=1,column=3)
yrL.grid(row=1, column=4)
yrE.grid(row=1,column=5)


def find_day():
    date = int(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())
    dob = datetime(day=date, month = mon, year = year)

    time_now = datetime.now()
    time_diff = time_now - dob

    dys = Label(app, text=f'You Lived {time_diff.days} days!',background=bg, foreground=fg)
    dys.grid(row=3, column=0, columnspan=4)

def find_sec():
    date = int(dayE.get())
    mon = int(monE.get())
    year = int(yrE.get())
    dob = datetime(day=date, month = mon, year = year)

    time_now = datetime.now()
    time_diff = time_now - dob

    secs = Label(app, text=f'You lived {time_diff.total_seconds()} seconds!', background=bg, foreground=fg)
    secs.grid(row=4, column=0, columnspan=6)


dayB = Button(app, text='Total Days', command=find_day, background=bg, foreground=fg)
dayB.grid(row=2, column=0, columnspan=3)
secB = Button(app, text='Total seconds', command=find_sec, background=bg, foreground=fg)
secB.grid(row=2, column=3, columnspan=3)
app.mainloop()