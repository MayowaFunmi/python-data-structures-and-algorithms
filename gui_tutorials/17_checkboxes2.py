from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')


def show():
    my_label_a = Label(root, text=var_a.get()).pack()
    my_label_b = Label(root, text=var_b.get()).pack()
    my_label_c = Label(root, text=var_c.get()).pack()


var_a = StringVar()
var_b = StringVar()
var_c = StringVar()

c = Checkbutton(root, text='Mathematics', variable=var_a, onvalue='Mathematics', offvalue='No')
c.deselect()
c.pack()

d = Checkbutton(root, text='English Language', variable=var_b, onvalue='English Language', offvalue='No')
d.deselect()
d.pack()

e = Checkbutton(root, text='Physics', variable=var_c, onvalue='Physics', offvalue='No')
e.deselect()
e.pack()

my_button = Button(root, text='Choose Subjects', command=show).pack()
root.mainloop()