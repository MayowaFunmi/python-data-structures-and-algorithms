from tkinter import *
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk

root = Tk()
root.geometry("1350x750+0+0")
root.title("Train Transportation Ticket")
root.configure(background='black')


#==============================Variables==========================================================

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
Tax = StringVar()
SubTotal = StringVar()
Total = StringVar()
text_Input = StringVar()
Date1 = StringVar()
time1 = StringVar()
operator = ""

#==============================Date And Time==========================================================
Date1.set(time.strftime("%d/%m/%Y"))
time1.set(time.strftime("%H:%M:%S"))


#==============================Frame============================================================

Tops = Frame(root, width=1350, height=100, bd=14, relief='raise')
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief='raise')
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, relief='raise')
f2.pack(side=RIGHT)

frameTopRight = Frame(f2, width=440, height=650, bd=12, relief='raise')
frameTopRight.pack(side=TOP)
frameBottomRight = Frame(f2, width=440, height=50, bd=16, relief='raise')
frameBottomRight.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=8, relief='raise')
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=6, relief='raise')
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a, width=300, height=200, bd=16, relief='raise')
topLeft3.pack(side=RIGHT)

bottomLeft1 = Frame(f2a, width=450, height=450, bd=14, relief='raised')
bottomLeft1.pack(side=LEFT)
bottomLeft2 = Frame(f2a, width=450, height=450, bd=14, relief='raised')
bottomLeft2.pack(side=RIGHT)

#==============================Frame Colors============================================================
Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')
#==============================Title Label============================================================
lblTitle = Label(Tops, font=('arial', 40, 'bold'), text="Train Transport Ticketing Systems", bd=10, width=41, justify='center')
lblTitle.grid(row=0, column=0)

lblReceipt = Label(frameTopRight, font=('arial', 14, 'bold'), text="Travelling Ticketing System", relief='sunken', width=32, height=5, justify='center')
lblReceipt.grid(row=0, column=0)

lblClass1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Class", relief='sunken', width=10, justify='center')
lblClass1.grid(row=0, column=0)
lblClass2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=10, justify='center')
lblClass2.grid(row=1, column=0)

lblTicket1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Ticket", relief='sunken', width=8, justify='center')
lblTicket1.grid(row=0, column=1)
lblTicket2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblTicket2.grid(row=1, column=1)

lblAdult1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Adult", relief='sunken', width=8, justify='center')
lblAdult1.grid(row=0, column=2)
lblAdult2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblAdult2.grid(row=1, column=2)

lblChild1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Child", relief='sunken', width=8, justify='center')
lblChild1.grid(row=0, column=3)
lblChild2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblChild2.grid(row=1, column=3)

lblFrom1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='From', relief='sunken', width=8, justify='center')
lblFrom1.grid(row=2, column=1)
lblFrom2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblFrom2.grid(row=2, column=2)

lblTo1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='To', relief='sunken', width=8, justify='center')
lblTo1.grid(row=3, column=1)
lblTo2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblTo2.grid(row=3, column=2)

lblPrice1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='Price', relief='sunken', width=8, justify='center')
lblPrice1.grid(row=4, column=1)
lblPrice2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblPrice2.grid(row=4, column=2)

lblRefNo1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='Ref No', relief='sunken', width=8, justify='center')
lblRefNo1.grid(row=5, column=0)
lblRefNo2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblRefNo2.grid(row=6, column=2)

lblTime1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='Time', relief='sunken', width=8, justify='center')
lblTime1.grid(row=5, column=1)
lblTime2 = Label(frameBottomRight, font=('arial', 14, 'bold'), textvariable=time1, relief='sunken', width=8, justify='center')
lblTime2.grid(row=6, column=1)

lblDate1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='Date', relief='sunken', width=8, justify='center')
lblDate1.grid(row=5, column=2)
lblDate2 = Label(frameBottomRight, font=('arial', 14, 'bold'), textvariable=Date1, relief='sunken', width=8, justify='center')
lblDate2.grid(row=6, column=2)

lblRoute1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text='Route', relief='sunken', width=8, justify='center')
lblRoute1.grid(row=5, column=3)
lblRoute2 = Label(frameBottomRight, font=('arial', 14, 'bold'), relief='sunken', width=8, justify='center')
lblRoute2.grid(row=6, column=3)



#==============================Functions==========================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""

#==============================Create Widgets topLeft1==========================================================

lblClass = Label(topLeft1, font=('arial', 22, 'bold'), text='Class', bd=8)
lblClass.grid(row=0, column=0, sticky=W)
chkStandard = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Standard', variable=var1, onvalue=1, offvalue=0)
chkStandard.grid(row=1, column=0, sticky=W)
chkEconomy = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Economy', variable=var2, onvalue=1, offvalue=0)
chkEconomy.grid(row=2, column=0, sticky=W)
chkFirstClass = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='First Class', variable=var3, onvalue=1, offvalue=0)
chkFirstClass.grid(row=3, column=0, sticky=W)

#==============================Create Widgets topLeft2==========================================================
lblSelect = Label(topLeft3, font=('arial', 20, 'bold'), text='Destination Selector', bd=8)
lblSelect.grid(row=0, column=0, sticky=W, columnspan=2)
lblDestination = Label(topLeft3, font=('arial', 20, 'bold'), text='Destination', bd=4)
lblDestination.grid(row=1, column=0, sticky=W)

cboDestination = ttk.Combobox(topLeft3, textvariable=var4, state='readonly', font=('arial', 20, 'bold'), width=8)
cboDestination['value'] = ('', 'Kilburn', 'Preston', 'Oxford', 'Leeds', 'Brixton')
cboDestination.current(0)
cboDestination.grid(row=1, column=1)

chkAdult = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Adult', variable=var5, onvalue=1, offvalue=0)
chkAdult.grid(row=2, column=0, sticky=W)
chkChild = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Child', variable=var6, onvalue=1, offvalue=0)
chkChild.grid(row=3, column=0, sticky=W)

#==============================Ticket==========================================================
lblClass = Label(topLeft2, font=('arial', 22, 'bold'), text='Ticket Type', bd=8)
lblClass.grid(row=0, column=0, sticky=W)

chkSingle = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Single', variable=var10, onvalue=1, offvalue=0)
chkSingle.grid(row=1, column=0, sticky=W)
entSingle = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var7, bd=2, width=8)
entSingle.grid(row=1, column=1, sticky=W)

chkReturn = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Return', variable=var2, onvalue=1, offvalue=0)
chkReturn.grid(row=2, column=0, sticky=W)
entReturn = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var8, bd=2, width=8)
entReturn.grid(row=2, column=1, sticky=W)

lblComment = Label(topLeft2, font=('arial', 22, 'bold'), text='Comment', bd=8)
lblComment.grid(row=3, column=0, sticky=W)
entComment = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var9, bd=2, width=8)
entComment.grid(row=3, column=1, sticky=W)

#==============================Calculator==========================================================
txtDisplay = Entry(bottomLeft2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=8, bg='powder blue', justify='right')
txtDisplay.grid(columnspan=4)

#=======buttons
#----------------------------------------------------------------------------------------------------------------------------------
btn7 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=7, bg='powder blue', command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=8, bg='powder blue', command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=9, bg='powder blue', command=lambda: btnClick(9)).grid(row=2, column=2)
Addition = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='+', bg='powder blue', command=lambda: btnClick('+')).grid(row=2, column=3)
#----------------------------------------------------------------------------------------------------------------------------------
btn4 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=4, bg='powder blue', command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=5, bg='powder blue', command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=6, bg='powder blue', command=lambda: btnClick(6)).grid(row=3, column=2)
Subtraction = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='-', bg='powder blue', command=lambda: btnClick('-')).grid(row=3, column=3)
#----------------------------------------------------------------------------------------------------------------------------------
btn1 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=1, bg='powder blue', command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=2, bg='powder blue', command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=3, bg='powder blue', command=lambda: btnClick(3)).grid(row=4, column=2)
Multiply = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='*', bg='powder blue', command=lambda: btnClick('*')).grid(row=4, column=3)
#----------------------------------------------------------------------------------------------------------------------------------
btn0 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text=0, bg='powder blue', command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='C', bg='powder blue', command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='=', bg='powder blue', command=btnEqualsInput).grid(row=5, column=2)
Division = Button(bottomLeft2, padx=8, pady=8, bd=8, fg='black', font=('arial', 10, 'bold'), width=4,
              text='/', bg='powder blue', command=lambda: btnClick("/")).grid(row=5, column=3)
#----------------------------------Tax, SubTotal And Total--------------------------------------------------------------------------
lblStateTax = Label(bottomLeft1, font=('arial', 16, 'bold'), text='State Tax', bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(bottomLeft1, font=('arial', 16, 'bold'), text='Sub Total', bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(bottomLeft1, font=('arial', 16, 'bold'), text='Total Cost', bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="#ffffff", justify='right')
txtTotalCost.grid(row=5, column=3)
#----------------------------------------------------------------------------------------------------------------------------------
"""
lblSPace = Label(bottomLeft1, font=('arial', 24, 'bold'), text="    \n        ", bd=16, anchor='w')
lblSPace.grid(row=6, column=2)

lblSPace = Label(bottomLeft2, font=('arial', 24, 'bold'), text="    \n        ", bd=16, anchor='w')
lblSPace.grid(row=6, columnspan=4)

#==========================================Information===================================================================
lblreceipt = Label(frameBottomRight, font=('arial', 24, 'bold'), text='Receipt', bd=2, anchor='w')
lblreceipt.grid(row=9, column=0, columnspan=4)

txtReceipt =  Text(frameBottomRight, width=40, height=7, bg='white', bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=10, column=0, columnspan=4)

"""
#----------------------------------------------------------------------------------------------------------------------------------
lReceipt = Label(frameBottomRight, font=('arial', 12, 'bold'), bd=2, anchor='w')
lReceipt.grid(row=7, column=0, sticky=W)

btnTotal = Button(frameBottomRight, text='Convert', padx=2, pady=2, bd=2, fg='black', font=('arial', 12, 'bold'), width=6, height=1).grid(row=8, column=0)

btnclear = Button(frameBottomRight, text='Clear', padx=2, pady=2, bd=2, fg='black', font=('arial', 12, 'bold'), width=6, height=1).grid(row=8, column=1)

btnReset = Button(frameBottomRight, text='Reset', padx=2, pady=2, bd=2, fg='black', font=('arial', 12, 'bold'), width=6, height=1).grid(row=8, column=2)

btnExit = Button(frameBottomRight, text='Exit', padx=2, pady=2, bd=2, fg='black', font=('arial', 12, 'bold'), width=6, height=1).grid(row=8, column=3)

mainloop()