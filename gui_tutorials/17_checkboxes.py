from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')


def show():
    my_label = Label(root, text=var.get()).pack()


var = IntVar()
c = Checkbutton(root, text='Check this now, i dare you', variable=var)
c.pack()

my_button = Button(root, text='Show Selection', command=show).pack()
root.mainloop()