from tkinter import *
from PIL import Image,ImageTk

app = Tk()
app.title('Icon')
app.geometry('200x200')
app.iconbitmap(r'GUI/Python.ico')

img = ImageTk.PhotoImage(Image.open(r'GUI/python.jpg'))
lbl = Label(app, image=img)
lbl.pack()


app.mainloop()