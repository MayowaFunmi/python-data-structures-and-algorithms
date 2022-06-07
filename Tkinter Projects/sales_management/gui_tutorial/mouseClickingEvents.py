"""Mouse Clicking Events
Clicking events are of 3 different types namely leftClick, middleClick, and rightClick.

Now, you will learn how to call a particular function based on the event that occurs.

Run the following program and click the left, middle, right buttons to calls a specific function.
That function will create a new label with the mentioned text.
"""
import tkinter

window = tkinter.Tk()
window.title("GUI")

#creating 3 different functions for 3 events
def left_click(event):
    tkinter.Label(window, text = "Left Click!").pack()

def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()

def right_click(event):
    tkinter.Label(window, text = "Right Click!").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()