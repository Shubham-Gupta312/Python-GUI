from tkinter import *

app = Tk()
app.title('Length Converter')
app.geometry('350x150')

scale = ['meter', 'inches', 'foot']

_from = StringVar()
from_menu = OptionMenu(app, _from, *scale)
from_menu.grid(row=0,column=0, pady=5)


lbl = Label(app, text='Convert to')
lbl.grid(row=0,column=1,pady=5)


to_ = StringVar()
to_menu = OptionMenu(app, to_, *scale)
to_menu.grid(row=0, column=2, pady=5)


numl = Label(app, text='Enter the Number')
numl.grid(row=1, column=0,columnspan=2, pady=5)

numE = Entry(app)
numE.grid(row=1, column=2, columnspan=2, pady=5)


# Conerting Function

def converter():
    From = _from.get()
    To = to_.get()
    num = int(numE.get())

    # Scales:
    # 1 meter = 39.37 inches
    # 1 meter = 3.28 foot
    # 1 foot = 12 inches

    if From == 'meter' and To == 'inches':
        conv_num = num * 39.37
    elif From == 'meter' and To == 'foot':
        conv_num = num * 3.28
    elif From == 'inches' and To == 'meter':
        conv_num = num / 39.37
    elif From == 'inches' and To == 'foot':
        conv_num = num / 12
    elif From == 'foot' and To == 'meters':
        conv_num = num / 3.28
    elif From == 'foot' and To == 'inches':
        conv_num = num * 12
    else:
        conv_num = num


    conv_numL = Label(app, text=round(conv_num, 2), width=5)
    conv_numL.grid(row=1, column=4, pady=5)


conB = Button(app, text='Convert', command=converter)
conB.grid(row=2, column=0, pady=5)
app.mainloop()
