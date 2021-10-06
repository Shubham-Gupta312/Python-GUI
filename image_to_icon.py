from tkinter import *

app = Tk()
app.title('Icon Converter')
app.geometry('300x200')

def open_img():
    from PIL import Image
    from tkinter import filedialog

    global img

    app.img_dir = filedialog.askopenfilename(initialdir='E:', title='Selct Your Image', filetypes=(('Png Image', '*.png'),('JPG Image','*.jpg'),('All files','*.*')))
    img = Image.open(app.img_dir)

#  -------->>>  Convert Image to Icon and save it
def img_con():
    from PIL import Image
    img.save(f'{ico_name.get()}.ico', format='ICO', sizes = [(ico_size.get(), ico_size.get())])

    success = Toplevel()
    success.title('Success')

    msg = Label(success, text='Conversion Successfully!')
    msg.pack()

    success.mainloop()

#  --------->>>>>> Preview the icon

def preview():
    prev = Toplevel()
    prev.title('Icon Preview')
    prev.iconbitmap(f'{ico_name.get()}.ico')

    prev_lbl = Label(prev, text='Check Your Icon!')
    prev_lbl.pack()

    prev.mainloop()


chooseL = Label(app, text='Select Your Image: ')
chooseL.grid(row=0, column=0)

chooseB = Button(app, text='Choose', command=open_img)
chooseB.grid(row=0,column=1)

sizeL = Label(app, text='Select a size for icon')
sizeL.grid(row=1, column=0)

ico_size = IntVar()
size_opt = [16,24,32,48,64, 128,255]
siz_menu = OptionMenu(app, ico_size, *size_opt)
siz_menu.grid(row=1, column=1)
ico_size.set(32)


# ------------->>>>>>>>>>  Icon Name Label
nam_lbl = Label(app, text='Enter the Icon Name: ')
nam_lbl.grid(row=2, column=0)

ico_name = Entry(app)
ico_name.grid(row=2, column=1)

# ------------------->>>>>>>>>>>>>>>>  Convert Button
conB = Button(app, text='Convert', command=img_con)
conB.grid(row=3, column=0)


# ---------------------->>>>>>>>>>>>>>>  Preview Button

prevB = Button(app, text='Preview', command=preview)
prevB.grid(row=3, column=1)

app.mainloop()