import tkinter

window = tkinter.Tk()
window.title("GUI")

# creating 3 simple Labels containing any text

# sufficient width
tkinter.Label(window, text = "Testing My GUI", fg = "white", bg = "orange").pack()

# width of X
tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill = "x")

# height of Y
tkinter.Label(window, text = "Taking all available Y height", fg = "white", bg = "black").pack(side = "right", fill = "y")

window.mainloop()