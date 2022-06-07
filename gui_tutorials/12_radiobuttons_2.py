from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')

modes = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion'),
]

pizza = StringVar()
pizza.set('Pepperoni')
for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text='Click Me', command=lambda: clicked(pizza.get()))
myButton.pack()



root.mainloop()