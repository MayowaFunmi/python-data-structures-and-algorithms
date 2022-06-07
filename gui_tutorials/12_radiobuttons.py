from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')

r = IntVar()
r.set('2')

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=r.get())     # from r.set('2')
myLabel.pack()

myButton = Button(root, text='Click Me', command=lambda: clicked(r.get()))
myButton.pack()



root.mainloop()