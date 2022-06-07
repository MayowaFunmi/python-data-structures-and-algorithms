from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title('Affable Digital Services')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno('This is tkinter popup', 'Do you want to continue?')
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text='Continue Working!!!').pack()
    else:
        Label(root, text='STOP!!!').pack()


Button(root, text='PopUp', command=popup).pack()
root.mainloop()