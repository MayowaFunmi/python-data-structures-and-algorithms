"""
Steps:-

import the module tkinter.
Initialize the window manager with the tkinter.Tk() method and assign it to a variable window. This method creates a blank window with close, maximize and minimize buttons.
Rename the title of the window as you like with the window.title(title_of_the_window).
Label is used to insert some objects into the window. Here, we are adding a Label with some text.
pack() attribute of the widget is used to display the widget in a size it requires.
Finally, the mainloop() method to display the window until you manually close it.
"""
import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Hello World!\n Welcome to my Graphical User Interface Project").pack()
window.mainloop()