from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='/home', title='Select A File',
                                               filetypes=(('all files', '.*'), ('png files', '*.png')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text='Open File', command=open).pack()


root.mainloop()