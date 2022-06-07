from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')
vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slider():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text='Click Me', command=slider).pack()
root.mainloop()