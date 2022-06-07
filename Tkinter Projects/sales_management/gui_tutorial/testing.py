from tkinter import *
window = Tk()
window.title("Testing Entry function")
window.configure(background = "black")

#create label Ll
Ll = Label(window, text = "Dominion", font = "none 12 bold", bg = "yellow", fg = "green").grid(row = 0, column = 0)

#create button bt
bt = Button(window, text = "ENTER", bg = "orange", fg = "red").grid(row = 1, column = 1)

#write a function to be excuted when enter button is clicked
def clicked():
    Ll.config(text = "Button was clicked!!")

bt = Button(window, text = "Enter", command = clicked).grid(row = 2, column = 0)
window.mainloop()