from tkinter import *
window = Tk()
window.title("My Desktop App")


#to print out users' input

#create an entry box
def program():
    res = myText.get() #get user input
    myLabel = Label(window, text ="You just entered " + res, fg = "black", bg = "orange", font = ("arial", 14, "italic")).grid(row = 3)

myText = StringVar() #converts user input to string to be gotten for display

Label(window, text= "Enter your text: ").grid(row = 0)
text = Entry(window, textvariable = myText).grid(row = 0, column = 1)#stores user input as "myText". create a button to click to display the text
myBut = Button(window, text = "Enter", fg = "blue", bg = "yellow", font = ("calibri", 12, "italic"), command = program).grid(row = 2)


#create an app that prints out users' username and pass word

def reply():
    res = fullname.get()
    res1 = username.get()
    res2 = password.get()
    myLabel1 = Label(window, text = "Welcome, " + res + " , \nYour Username is " + res1 + " and your Password is " + res2).grid(row = 9)
    
    
fullname = StringVar()
username = StringVar()
password = StringVar()

#create a label for fullname
la = Label(window, text = "Name (in full) : ").grid(row = 4)

#create an entry box for fullname
en = Entry(window, textvariable = fullname, width = 20).grid(row = 4, column = 1, sticky = W)

#create a label for username
label1 = Label(window, text = "Username : ").grid(row = 5)

#create entry1 for label1
entry1 = Entry(window, textvariable = username, width = 20).grid(row = 5, column = 1, sticky = W)

#create label for paasword
label2 = Label(window, text = "Password: ").grid(row = 6)

#create entry for password
entry2= Entry(window, textvariable = password, width = 10).grid(row = 6, column = 1, sticky = W)

#create checkbutton
var1 = IntVar()

Checkbutton(window, text = "Keep Me Logged in", bg = "blue", fg = "white", font = ("calibri", 10, "italic"), variable = var1).grid(row = 7, column = 1)
#create button for submit

but = Button(window, text = "SUBMIT", fg = "red", bg = "white", font = ("arial", 12, "bold"), command = reply).grid(row = 8,  column = 1)



window.mainloop()