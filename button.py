from tkinter import *

app = Tk()

app.title('Button')

app.geometry('200x200')

display = Label(app, text = "We Learn Tkinter Module")
display.pack()

def show():
    msg = Label(app, text='Have a nice day!')
    msg.pack()

b = Button(app, text='click' , command=show)
b.pack()

app.mainloop()