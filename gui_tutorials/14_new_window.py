from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')


def open():
    # create new window
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    my_img = ImageTk.PhotoImage(Image.open('images/img_1.jpg').resize((350, 350), Image.ANTIALIAS))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text='X', command=top.destroy).pack()


btn = Button(root, text='Open New Window', command=open).pack()
root.mainloop()