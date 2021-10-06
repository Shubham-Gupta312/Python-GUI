from tkinter import *
app = Tk()
app.title('Input')
app.geometry('200x200')

inp = Entry(app)
inp.pack()

def show():
    Inp = inp.get()
    msg = Label(app, text=Inp)
    msg.pack()

b = Button(app, text='Show', command=show)
b.pack()

app.mainloop()