from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

app = Tk()
app.title('Image')
app.geometry('250x200')

def img_select():
    global img

    app.fname = filedialog.askopenfilename(initialdir='PYTHON', title='Select a File', filetypes=(('Png Images', '*.png'), ('JPG Images', '*.jpg'),('All Files', '*.*')))
    b.destroy()
    img = ImageTk.PhotoImage(Image.open(app.fname))
    lbl = Label(app, image=img)
    lbl.pack()

b = Button(app, text='View', command=img_select)
b.pack()

app.mainloop()