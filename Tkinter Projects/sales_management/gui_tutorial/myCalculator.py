#DJ Oamen
import sys
from tkinter import *
root = Tk()
root.title("My Calculator")
root.configure(background ="yellow")
frame = Frame(root).pack()

def clear():
    textDisplay.delete(0, END)
    return
    
    
    
num1 = StringVar()


textDisplay = Entry(frame, textvariable = num1, bd = 15, width = 100, font = 30).pack(side = TOP)


topframe = Frame(root).pack(side = TOP)
button1 = Button(topframe, padx =16, pady = 16, bd = 8, text = "1", fg = "black").pack(side = LEFT)

button2 = Button(topframe, padx =16, pady = 16, bd = 8, text = "2", fg = "black").pack(side = LEFT)

button3 = Button(topframe, padx =16, pady = 16, bd = 8, text = "3", fg = "black").pack(side = LEFT)

button4 = Button(topframe, padx =16, pady = 16, bd = 8, text = "4", fg = "black").pack(side = LEFT)

frame1 = Frame(root).pack(side = TOP)

button1 = Button(frame1, padx =16, pady = 16, bd = 8, text = "5", fg = "black").pack(side = LEFT)

button2 = Button(frame1, padx =16, pady = 16, bd = 8, text = "6", fg = "black").pack(side = LEFT)

button3 = Button(frame1, padx =16, pady = 16, bd = 8, text = "7", fg = "black").pack(side = LEFT)

button4 = Button(frame1, padx =16, pady = 16, bd = 8, text = "8", fg = "black").pack(side = LEFT)

frame2 = Frame(root).pack(side = TOP)

button1 = Button(frame2, padx =16, pady = 16, bd = 8, text = "9", fg = "black").pack(side = LEFT)

button2 = Button(frame2, padx =16, pady = 16, bd = 8, text = "0", fg = "black").pack(side = LEFT)

button3 = Button(frame2, padx =16, pady = 16, bd = 8, text = "C", fg = "black", command = clear).pack(side = LEFT)

button4 = Button(frame2, padx =16, pady = 16, bd = 8, text = "=", fg = "black").pack(side = LEFT)

frame3 = Frame(root).pack(side = TOP)

button1 = Button(frame3, padx =16, pady = 16, bd = 8, text = "X", fg = "black").pack(side = LEFT)

button2 = Button(frame3, padx =16, pady = 16, bd = 8, text = "/", fg = "black").pack(side = LEFT)

button3 = Button(frame3, padx =16, pady = 16, bd = 8, text = "-", fg = "black").pack(side = LEFT)

button4 = Button(frame3, padx =16, pady = 16, bd = 8, text = "1+", fg = "black").pack(side = LEFT)

root.mainloop()