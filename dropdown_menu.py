from tkinter import *

app = Tk()
app.title('DropDown Menu')
app.geometry('250x200')


menu_ch = StringVar()
option = ['red', 'white','green','yellow', 'grey','black','royal Blue']
menu = OptionMenu(app, menu_ch, *option)
menu.pack()

def show():
    msg = Label(app, text='         ',background=(menu_ch.get()).capitalize())
    msg.pack()

b = Button(app, text='Show', command=show)
b.pack()

app.mainloop()