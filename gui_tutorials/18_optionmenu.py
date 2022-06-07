from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

clicked = StringVar()
clicked.set('Choose Days Of The Week')

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text='SHow Selection', command=show).pack()

root.mainloop()