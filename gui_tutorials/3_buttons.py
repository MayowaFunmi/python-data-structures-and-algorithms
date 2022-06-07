from tkinter import *

root = Tk()

# let myButton do something


def myClick():
    myLabel = Label(root, text='I just Clicked You!')
    myLabel.pack()


myButton = Button(root, text='Click Me!', padx=50, pady=10, command=myClick, fg='blue', bg='red')
myButton.pack()


root.mainloop()