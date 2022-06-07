from tkinter import *

root = Tk()

e = Entry(root, width=50, bg='black', fg='white', borderwidth=5)
e.pack()
# use e.get() to get the entered text
e.insert(0, "Enter Your Name")  # placeholder

# let myButton do something
def myClick():
    disp_text = "Hello " + e.get()
    myLabel = Label(root, text=disp_text)
    myLabel.pack()


myButton = Button(root, text='Enter Your Name!', padx=50, pady=10, command=myClick, fg='blue', bg='red')
myButton.pack()


root.mainloop()