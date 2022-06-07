from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Affable Digital Services')
#root.iconbitmap('gui_tutorials/images/icon.ico')

my_img = ImageTk.PhotoImage(Image.open('images/portfolio_pic.png'))
my_label = Label(root, image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()