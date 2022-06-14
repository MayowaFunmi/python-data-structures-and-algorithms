from tkinter import *
import sqlite3


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')

# create or connect a database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# create submit function
def submit():
    # create or connect a database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              })
    conn.commit()
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # create or connect a database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[6]) + ": " + str(record[0]) + " " + str(record[1]) + '\n'
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    conn.commit()
    conn.close()


# create delete function
def delete():
    # create or connect a database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # delete a record
    c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)
    conn.commit()
    conn.close()

# create table
"""
c.execute('''
    CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )
''')
"""

# create text boxes and labels
f_name_label = Label(root, text='First Name:')
f_name_label.grid(row=0, column=0, pady=(10, 0))
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name_label = Label(root, text='Last Name:')
l_name_label.grid(row=1, column=0)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address_label = Label(root, text='Address:')
address_label.grid(row=2, column=0)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city_label = Label(root, text='City:')
city_label.grid(row=3, column=0)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state_label = Label(root, text='State:')
state_label.grid(row=4, column=0)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode_label = Label(root, text='Zip Code:')
zipcode_label.grid(row=5, column=0)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box_label = Label(root, text='ID Number: ')
delete_box_label.grid(row=9, column=0, pady=5)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# create submit button
submit_btn = Button(root, text='Add Record To database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# create a query button
query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button
delete_btn = Button(root, text='Delete Records', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

conn.commit()
conn.close()

root.mainloop()