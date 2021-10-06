from tkinter import *
from random import randint

app = Tk()
app.title('Random Number Generator')
app.geometry('250x250')

msg = Label(app, text='Generate a random Number')
msg.pack()

def show():
    msg1 = Label(app, text=randint(1,100))
    msg1.pack()

b = Button(app, text='Generate', command=show)
b.pack()

app.mainloop()