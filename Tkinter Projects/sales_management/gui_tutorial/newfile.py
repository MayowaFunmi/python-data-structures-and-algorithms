from tkinter import *
#create a window
window = Tk()
window.title("My Python GUI course")

#using the place method
Label(window, text = "I am Dominion", bg = "orange", fg = "black").place(x = 0, y = 10)


#Button and function
#first, define the function to execute the command
def hello():
    res = Label(window, text =" Hello There !\nWelcome to Dominion IT service!!\nHow may we help you?", font =( "calibri", 12, "italic")).pack()

myButton1 = Button(window, text = "Enter", fg = "black", bg = "green", command = hello).place(y = 50)











#display the app
window.mainloop()