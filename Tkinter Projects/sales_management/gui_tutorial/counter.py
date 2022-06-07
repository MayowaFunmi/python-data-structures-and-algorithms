from tkinter import *
root = Tk()
root.title("Creating Counter")


from time import sleep
def counter_label(label):
    for count in range(1000, -1, -1): # Range 10, 9, 8, ..., 0
        label = count # Display the count
        sleep(1) # Suspend execution for 1 second
"""counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text = str(counter))
        label.after(1000, count)
        counter()"""


label = Label(root, fg = "dark green").pack()
counter_label(label) #to display the counter on the label

button = Button(root, text = "stop", width = 40, command = root.destroy).pack()

root.mainloop()