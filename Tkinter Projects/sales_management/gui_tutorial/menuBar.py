from tkinter import *
window = Tk()
window.title("Adding Menu Bar")

def newfile1():
    myfile = Label(text = "Open New File").pack()
    
def newfile2():
    #open file manager
    file1 = filedialog.askopenfile()
    #get file name and save in file2
    file2 = file1.name
    f = open(file2)
    Label(window, text = f.read(), font = ("arial", 10, "bold"), bg = "yellow", fg = "green").pack()
    
def mbox():
    messagebox.showinfo(title = "save", message = "Are you sure to save this file?")
    
def mquit():
    mess = messagebox.askyesno(title = "quit", message = "Confirm Quit")
    if mess == 1:
        window.destroy()


#add menubar and menulist
myMenu = Menu() #menu list

listone = Menu() #menu list

listone.add_command(label = "New File", command = newfile1)
listone.add_command(label = "Open File", command = newfile2)
listone.add_command(label = "Save File", command = mbox)
listone.add_command(label = "Quit", command = mquit)


listtwo = Menu()
listtwo.add_command(label = "Undo")
listtwo.add_command(label = "Redo")

listthree = Menu()
listthree.add_command(label = "PDF")
listthree.add_command(label = "doc")
listthree.add_command(label = "mp3")

listfour = Menu()
listfour.add_command(label = "Run File")


myMenu.add_cascade(label = "File", menu = listone)
myMenu.add_cascade(label = "Edit", menu = listtwo)
myMenu.add_cascade(label = "Format", menu = listthree)
myMenu.add_cascade(label = "Run", menu = listfour)

window.config(menu = myMenu)





window.mainloop()