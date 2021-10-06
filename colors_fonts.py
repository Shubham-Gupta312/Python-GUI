from tkinter import *
from random import choice


app = Tk()
app.title('Element Picker')
app.geometry('300x250')
app['background'] = 'grey'

inp = Entry(app, background='yellow', relief='raised', borderwidth=3)
inp.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

def pick():
    Inp = (inp.get()).split(',')
    msg = Label(app, text=choice(Inp), font=('Courier', 13), background='grey', foreground='black', relief='sunken',borderwidth=4, width=7)
    msg.grid(row=0, column=2,padx=20, pady=5) 

    if quitb['state'] == DISABLED:
        quitb['state'] = NORMAL

b = Button(app, text='Choose', command=pick,relief='groove',borderwidth=5,background='grey')
b.grid(row=1, column=0,padx=20, pady=5)

quitb = Button(app, text='Close', command=app.quit,background='red',foreground='white', state=DISABLED)
quitb.grid(row=1, column=1,padx=20, pady=5)

app.mainloop()
