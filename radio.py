from tkinter import *
app = Tk()
app.title('Radio Boxes')
app.geometry('250x150')

rad = StringVar()

rb1 = Radiobutton(app,text='Option 1',variable=rad, value='RB1 selected')
rb2 = Radiobutton(app,text='Option 2',variable=rad, value='RB2 selected')
rb1.deselect()
rb2.deselect()
rb1.pack()
rb2.pack()

def show():
    msg = Label(app, text=rad.get())
    msg.pack()

b = Button(app,text='Show', command=show)
b.pack()

app.mainloop()