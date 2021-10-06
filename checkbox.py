from tkinter import *

app = Tk()
app.title('CheckBox')
app.geometry('250x100')

check = StringVar()
chk = Checkbutton(app, text='Checkbox', variable=check,onvalue='Yes', offvalue='Nope')
chk.deselect()
chk.pack()

def show():
    msg = Label(app, text=check.get())
    msg.pack()

b = Button(app, text='show', command=show)
b.pack()

app.mainloop()