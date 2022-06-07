from tkinter import *
import time
import datetime
import pygame, sys, random
import tkinter.messagebox

pygame.init()
root = Tk()
root.title('Sales Management System')
root.geometry('1360x768')
root.configure(background='white')
#print(root.winfo_screenheight())
#print(root.winfo_screenwidth())

#===================== Frame ===================================
ABC = Frame(root, bg='powder blue', bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg='Cadet Blue', bd=10, relief=RIDGE)
ABC1.grid(row=0, column=0, columnspan=4, sticky=W)

ABC2 = Frame(ABC, bg='powder blue', bd=10, relief=RIDGE)
ABC2.grid(row=1, column=0, sticky=W)

ABC3 = Frame(ABC, bg='powder blue', bd=10, relief=RIDGE)
ABC3.grid(row=1, column=1, sticky=W)

ABC4 = Frame(ABC, bg='powder blue', bd=10, relief=RIDGE)
ABC4.grid(row=1, column=2, sticky=W)

ABC5 = Frame(ABC4, bg='powder blue', bd=10, relief=RIDGE)
ABC5.grid(row=0, column=0, sticky=W)

ABC6 = Frame(ABC4, bg='powder blue', bd=10, relief=RIDGE)
ABC6.grid(row=1, column=0, columnspan=4, sticky=W)


#===================== Variables ===================================
Date1 = StringVar()
Time1 = StringVar()
Receipt_Ref = StringVar()
Tax = StringVar()
Subtotal = StringVar()
Total = StringVar()

Jeans_Jeggers = StringVar()
Coats_Jackets = StringVar()
Sportwear = StringVar()
Dresses = StringVar()
Skirts = StringVar()
Swimwear = StringVar()
School_Uniform = StringVar()
Pyjamas_Dressing = StringVar()

Jackets_Blazers = StringVar()
Formal_Trousers = StringVar()
Formal_Shirts = StringVar()
Mens_Boots = StringVar()
Bed_Sheet = StringVar()
Pillows_Cases = StringVar()
Patterned_Bedding = StringVar()
Mattress_Protectors = StringVar()

Jeans_Jeggers.set('0')
Coats_Jackets.set('0')
Sportwear.set('0')
Dresses.set('0')
Skirts.set('0')
Swimwear.set('0')
School_Uniform.set('0')
Pyjamas_Dressing.set('0')

Jackets_Blazers.set('0')
Formal_Trousers.set('0')
Formal_Shirts.set('0')
Mens_Boots.set('0')
Bed_Sheet.set('0')
Pillows_Cases.set('0')
Patterned_Bedding.set('0')
Mattress_Protectors.set('0')


#===================== Function Declarations ===================================


def digital_clock():
    c_time = time.strftime("%H:%M:%S %p")
    lblTime.config(text=c_time)
    lblTime.after(1000, digital_clock)


def iExit():
    iExit = tkinter.messagebox.askyesno("Sales Management System", "Confirm Exit")
    if iExit > 0:
        root.destroy()
        return


def Reset():
    txtReceipt.config(state='normal')
    txtReceipt.delete('1.0', END)
    Jeans_Jeggers.set('0')
    Coats_Jackets.set('0')
    Sportwear.set('0')
    Dresses.set('0')
    Skirts.set('0')
    Swimwear.set('0')
    School_Uniform.set('0')
    Pyjamas_Dressing.set('0')

    Jackets_Blazers.set('0')
    Formal_Trousers.set('0')
    Formal_Shirts.set('0')
    Mens_Boots.set('0')
    Bed_Sheet.set('0')
    Pillows_Cases.set('0')
    Patterned_Bedding.set('0')
    Mattress_Protectors.set('0')


def Total():
    item1 = float(Jeans_Jeggers.get())
    item2 = float(Coats_Jackets.get())
    item3 = float(Sportwear.get())
    item4 = float(Dresses.get())
    item5 = float(Skirts.get())
    item6 = float(Swimwear.get())
    item7 = float(School_Uniform.get())
    item8 = float(Pyjamas_Dressing.get())

    item9 = float(Jackets_Blazers.get())
    item10 = float(Formal_Trousers.get())
    item11 = float(Formal_Shirts.get())
    item12 = float(Mens_Boots.get())
    item13 = float(Bed_Sheet.get())
    item14 = float(Pillows_Cases.get())
    item15 = float(Patterned_Bedding.get())
    item16 = float(Mattress_Protectors.get())

    price_of_item1 = ('N') + str('%.2f'%(item1 * 19.22))
    price_of_item2 = ('N') + str('%.2f'%(item2 * 69.99))
    price_of_item3 = ('N') + str('%.2f'%(item3 * 12.93))
    price_of_item4 = ('N') + str('%.2f'%(item4 * 12.99))
    price_of_item5 = ('N') + str('%.2f'%(item5 * 15.99))
    price_of_item6 = ('N') + str('%.2f'%(item6 * 22.99))
    price_of_item7 = ('N') + str('%.2f'%(item7 * 18.56))
    price_of_item8 = ('N') + str('%.2f'%(item8 * 9.22))
    price_of_item9 = ('N') + str('%.2f'%(item9 * 71.35))
    price_of_item10 = ('N') + str('%.2f'%(item10 * 32.21))
    price_of_item11 = ('N') + str('%.2f'%(item11 * 17.99))
    price_of_item12 = ('N') + str('%.2f'%(item12 * 70.49))
    price_of_item13 = ('N') + str('%.2f'%(item13 * 11.01))
    price_of_item14 = ('N') + str('%.2f'%(item14 * 11.67))
    price_of_item15 = ('N') + str('%.2f'%(item15 * 15.61))
    price_of_item16 = ('N') + str('%.2f'%(item16 * 20.99))

    price_of_women = (item1 * 19.22) + (item2 * 69.99) + (item3 * 12.93) + (item4 * 12.99)
    price_of_kid = (item5 * 15.99) + (item6 * 22.99) + (item7 * 18.56) + (item8 * 9.22)
    price_of_men = (item9 * 71.35) + (item10 * 32.21) + (item11 * 17.99) + (item12 * 70.49)
    price_of_homeware = (item13 * 11.01) + (item14 * 11.67) + (item15 * 15.61) + (item16 * 20.99)

    sub_total_items = ('N') + str('%.2f'%(price_of_women + price_of_kid + price_of_men + price_of_homeware))
    i_tax = ('N') + str('%.2f'%((price_of_women + price_of_kid + price_of_men + price_of_homeware) * 0.075))

    TT = (price_of_women + price_of_kid + price_of_men + price_of_homeware)
    TC = ((price_of_women + price_of_kid + price_of_men + price_of_homeware) * 0.075)
    TotalCost = ('N') + str('%.2f'%(TT + TC))

    txtReceipt.delete('1.0', END)
    x = random.randint(10345, 500276)
    randomRef = str(x)
    Receipt_Ref.set("BILL " + randomRef)
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t' + Receipt_Ref.get() + '\n' + Date1.get() + '\t\t\t\t' + Time1.get() + '\n')
    txtReceipt.insert(END, '-----------------------------------------------------------------------------' + '\n')
    txtReceipt.insert(END, 'Item:\t\t\t\t' + 'Cost of items' + '\n')
    txtReceipt.insert(END, '-----------------------------------------------------------------------------' + '\n')
    txtReceipt.insert(END, 'Jeans & Jeggers:\t\t\t\t' + price_of_item1 + '\n')
    txtReceipt.insert(END, 'Coats Jackets:\t\t\t\t' + price_of_item2 + '\n')
    txtReceipt.insert(END, 'Sports Wear:\t\t\t\t' + price_of_item3 + '\n')
    txtReceipt.insert(END, 'Dresses:\t\t\t\t' + price_of_item4 + '\n')
    txtReceipt.insert(END, 'Skirts:\t\t\t\t' + price_of_item5 + '\n')
    txtReceipt.insert(END, 'Swimwear:\t\t\t\t' + price_of_item6 + '\n')
    txtReceipt.insert(END, 'School Uniform:\t\t\t\t' + price_of_item7 + '\n')
    txtReceipt.insert(END, 'Pyjamas & Dressing:\t\t\t\t' + price_of_item8 + '\n')
    txtReceipt.insert(END, 'Jackets & Blazers:\t\t\t\t' + price_of_item9 + '\n')
    txtReceipt.insert(END, 'Formal Trousers:\t\t\t\t' + price_of_item10 + '\n')
    txtReceipt.insert(END, 'Formal Shirt:\t\t\t\t' + price_of_item11 + '\n')
    txtReceipt.insert(END, 'Mens Boot:\t\t\t\t' + price_of_item12 + '\n')
    txtReceipt.insert(END, 'Bed Sheet:\t\t\t\t' + price_of_item13 + '\n')
    txtReceipt.insert(END, 'Pillow Cases:\t\t\t\t' + price_of_item14 + '\n')
    txtReceipt.insert(END, 'Patterned Bedding:\t\t\t\t' + price_of_item15 + '\n')
    txtReceipt.insert(END, 'Mattress Protectors:\t\t\t\t' + price_of_item16 + '\n')
    txtReceipt.insert(END, 'Tax Paid:\t\t\t\t' + i_tax + '\n')
    txtReceipt.insert(END, 'SubTotal:\t\t\t\t' + sub_total_items + '\n')
    txtReceipt.insert(END, 'Total Cost:\t\t\t\t' + TotalCost + '\n')
    txtReceipt.config(state='disabled')


#===================== Date And Time ===================================
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S %p"))


lblDate = Label(ABC1, textvariable=Date1, font=('arial', 30, 'bold'), padx=9, pady=9, bd=5, bg='Cadet Blue', fg='Cornsilk',
                justify=CENTER).grid(row=0, column=0)

lblTitle = Label(ABC1, text="\tSales Management System\t", font=('arial', 30, 'bold'), padx=9, pady=9, bd=14, bg='Cadet Blue',
                 fg='Cornsilk', justify=CENTER).grid(row=0, column=1)

lblTime = Label(ABC1, textvariable=Time1, font=('arial', 30, 'bold'), padx=9, pady=9, bd=5, bg='Cadet Blue', fg='Cornsilk',
                justify=CENTER).grid(row=0, column=2)
#digital_clock()


#===================== Labels And Text Entries ===================================
lblWomen = Label(ABC2, text='Women', font=('arial', 20, 'bold'), pady=1, bd=8, bg='Cadet Blue', fg='Cornsilk', width=25,
                 justify=CENTER).grid(row=0, column=0, columnspan=4)
lblJeansJeggers = Label(ABC2, text='Jeans & Jeggers', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=1, column=0, sticky=W)
lblCoatsJackets = Label(ABC2, text='Coats Jackets', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=2, column=0, sticky=W)
lblSportWear = Label(ABC2, text='Sports Wear', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=3, column=0, sticky=W)
lblDresses = Label(ABC2, text='Dresses', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=4, column=0, sticky=W)
lblSkirts = Label(ABC2, text='Skirts', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=6, column=0, sticky=W)
lblSwimwear = Label(ABC2, text='Swimwear', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=7, column=0, sticky=W)
lblSchoolUniform = Label(ABC2, text='School Uniform', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=8, column=0, sticky=W)
lblPyjamasDressing = Label(ABC2, text='Pyjamas & Dressing', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=9, column=0, sticky=W)

#=====================  Text ===================================

txtJeans_Jeggers = Entry(ABC2, textvariable=Jeans_Jeggers, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=1, column=1, pady=1)
txtCoats_Jackets = Entry(ABC2, textvariable=Coats_Jackets, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=2, column=1, pady=1)
txtSportwear = Entry(ABC2, textvariable=Sportwear, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=3, column=1, pady=1)
txtDresses = Entry(ABC2, textvariable=Dresses, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=4, column=1, pady=1)
lblKids = Label(ABC2, text='Kids', font=('arial', 20, 'bold'), pady=1, bd=8, fg='Cornsilk', width=25, bg='Cadet Blue', justify=CENTER).grid(row=5, column=0, columnspan=4)
txtSkirts = Entry(ABC2, textvariable=Skirts, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=6, column=1, pady=1)
txtSwimwear = Entry(ABC2, textvariable=Swimwear, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=7, column=1, pady=1)
txtSchool_Uniform = Entry(ABC2, textvariable=School_Uniform, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=8, column=1, pady=1)
txtPyjamas = Entry(ABC2, textvariable=Pyjamas_Dressing, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=9, column=1, pady=1)

#================================================================================

lblMens = Label(ABC3, text='Men', font=('arial', 20, 'bold'), pady=1, bd=8, bg='Cadet Blue', fg='Cornsilk', width=25,
                 justify=CENTER).grid(row=0, column=0, columnspan=4)
lblJacketsBlazers = Label(ABC3, text='Jackets & Blazers', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=1, column=0, sticky=W)
lblFormalTrousers = Label(ABC3, text='Formal Trousers', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=2, column=0, sticky=W)
lblFormalShirts = Label(ABC3, text='Formal Shirt', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=3, column=0, sticky=W)
lblMensBoot = Label(ABC3, text='Mens Boot', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=4, column=0, sticky=W)
lblBedSheet = Label(ABC3, text='Bed Sheet', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=6, column=0, sticky=W)
lblPillowCases = Label(ABC3, text='Pillow Cases', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=7, column=0, sticky=W)
lblPatternedBedding = Label(ABC3, text='Patterned Bedding', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=8, column=0, sticky=W)
lblMattressProtectors = Label(ABC3, text='Mattress Protectors', font=('arial', 18, 'bold'), bg='powder blue', justify=LEFT).grid(row=9, column=0, sticky=W)

#=====================  Text ===================================

txtJackets_Blazers = Entry(ABC3, textvariable=Jackets_Blazers, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=1, column=1, pady=1)
txtFormal_Trousers = Entry(ABC3, textvariable=Formal_Trousers, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=2, column=1, pady=1)
txtFormal_Shirts = Entry(ABC3, textvariable=Formal_Shirts, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=3, column=1, pady=1)
txtMens_Boot = Entry(ABC3, textvariable=Mens_Boots, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=4, column=1, pady=1)
lblHomeware = Label(ABC3, text='Homeware', font=('arial', 20, 'bold'), pady=1, bd=8, fg='Cornsilk', width=25, bg='Cadet Blue', justify=CENTER).grid(row=5, column=0, columnspan=4)
txtBed_Sheet = Entry(ABC3, textvariable=Bed_Sheet, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=6, column=1, pady=1)
txtPillow_Cases = Entry(ABC3, textvariable=Pillows_Cases, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=7, column=1, pady=1)
txtPatterned_Bedding = Entry(ABC3, textvariable=Patterned_Bedding, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=8, column=1, pady=1)
txtMattress_Protectors = Entry(ABC3, textvariable=Mattress_Protectors, font=('arial', 18, 'bold'), bd=8, fg='black', width=12, justify=CENTER).grid(row=9, column=1, pady=1)

#=====================  Text ===================================
txtReceipt = Text(ABC5, height=24, width=45, bd=10, font=('arial', 9, 'bold'))
txtReceipt.grid(row=0, column=0)

#=====================  Button ===================================

btnTotal = Button(ABC6, command=Total, padx=16, pady=1, bd=4, fg='black', font=('arial', 14, 'bold'), width=7, bg='powder blue', text='Total')
btnTotal.grid(row=0, column=0)
btnReset = Button(ABC6, command=Reset, padx=16, pady=1, bd=4, fg='black', font=('arial', 14, 'bold'), width=7, bg='powder blue', text='Reset')
btnReset.grid(row=0, column=1)
btnExit = Button(ABC6, padx=16, command=iExit, pady=1, bd=4, fg='black', font=('arial', 14, 'bold'), width=7, bg='powder blue', text='Exit')
btnExit.grid(row=0, column=2)

root.mainloop()
