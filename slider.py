from tkinter import *

app = Tk()
app.title('Slider')
app.geometry('250x200')

sld_val = IntVar()
sld = Scale(app, from_=0, to=100, variable=sld_val, orient=HORIZONTAL)
sld.pack()

def show():
    msg = Label(app, text=sld_val.get())
    msg.pack()

b = Button(app, text='Show', command=show)
b.pack()

app.mainloop()