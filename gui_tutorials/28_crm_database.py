from tkinter import *
import sqlite3

root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')

# create or connect a database
conn = sqlite3.connect('affable.db')
c = conn.cursor()

# create a table
c.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        first_name text,
        last_name text,
        zipcode integer,
        price_paid integer,
        email text,
        address_1 text,
        address_2 text,
        city text,
        state text,
        country text,
        phone text,
        payment_method text,
        discount_code text
    )
''')


conn.commit()
conn.close()

# create a label
title_label = Label(root, text='Affable Customer Database', font=('Helvetica', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, pady='10')

# Create form to enter customer data
first_name_label = Label(root, text='First Name:').grid(row=1, column=0)
last_name_label = Label(root, text='Last Name:').grid(row=2, column=0)
address1_label = Label(root, text='Address 1:').grid(row=3, column=0)
address2_label = Label(root, text='Address 2:').grid(row=4, column=0)
city_label = Label(root, text='City:').grid(row=5, column=0)
state_label = Label(root, text='State:').grid(row=6, column=0)
zipcode_label = Label(root, text='Zip Code:').grid(row=7, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)
first_name_label = Label(root, text='First Name').grid(row=1, column=0)





root.mainloop()