from tkinter import *
window = Tk()
window2 = Tk() #create a second window

window.title("My Computer Science Glossary")
window.configure(background = "black")

#my photo
#photo1 = PhotoImage(file = "/storage/sdcard0/mypix.jgp")
#Label(window, image = photo1).grid(row = 0, column = 0, sticky = E)

#create a header label
Label(window, text = "Hello There!!! \nWelcome to my GUI world with python!", bg = "yellow", fg = "black").grid(row = 0, column = 0, sticky = W)

#create a label
Ll = Label(window, text= "\nEnter the word you would like a definition for: ", bg = "black", fg = "white", font = "Arial 12 bold").grid(row = 1, column = 0, sticky = W)


# create a function click()
def click():
    entered_text = myWord.get()#this will collect the text from the text entry box
    try:
        Label(window, text = my_compdictionary[entered_text], background = "white").grid(row = 5, column = 0, columnspan = 2, sticky = W)
    except:
        Label(window, text = "Sorry, there is match for the word!!!", bg = "red", fg = "white").grid(row = 5, column = 0, columnspan = 2, sticky = W)

myWord = StringVar() #convert user word to string

#create a text entry box
Entry(window, textvariable = myWord, width = 20, bg = "white").grid(row = 2, column = 0, sticky = W)



#add a submit button
Button(window, text = "SUBMIT", width = 6, command = click).grid(row = 3, column = 0, sticky = W)

#create another label
Label(window, text = "\nDefinition: ", bg = "black", fg = "white", font = "none 12 bold").grid(row = 4, column = 0, sticky = W)



#the dictionary
my_compdictionary = {'algorithm': 'step by step instructions to complete a task', 'bug': 'piece of codes that causes a program to fail'}

#Frame(window, text = "Frame", bg = "red", fg = "black").pack(side = bottom)


window.mainloop()