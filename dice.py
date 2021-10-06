from tkinter import *

app = Tk()
app.title('Dice Roller')


die = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'

}



dice = Label(app, text=die[0], font=('Times', 100), foreground='black')
dice.grid(row=0, column=0, padx=25)

def roll():
    from random import randint
    i = randint(1,6)
    msg = Label(app, text=die[i], font=('Times', 100), foreground='black', width=2)
    msg.grid(row=0, column=0, padx=25)


rollb = Button(app, text='Roll', command=roll)
rollb.grid(row=1, column=0)

app.mainloop()

