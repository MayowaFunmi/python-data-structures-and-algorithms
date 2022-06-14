from tkinter import *
import sqlite3


root = Tk()
root.title('Affable Digital Services')
root.geometry('1300x700')

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
    query_label.grid(row=12, column=0, columnspan=2)
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


def destroy():
    editor.destroy()

def update():
    # create or connect a database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_id
        })
    conn.commit()
    conn.close()
    #editor.destroy()
    close_btn = Button(editor, text='Close Window', command=destroy)
    close_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
    msg_label = Label(editor, text='Your changes saved successfully')
    msg_label.grid(row=7, column=0)


# create update function
def edit():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.geometry('400x600')

    # create global variables

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create text boxes and labels
    f_name_label = Label(editor, text='First Name:')
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_label = Label(editor, text='Last Name:')
    l_name_label.grid(row=1, column=0)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_label = Label(editor, text='Address:')
    address_label.grid(row=2, column=0)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_label = Label(editor, text='City:')
    city_label.grid(row=3, column=0)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_label = Label(editor, text='State:')
    state_label.grid(row=4, column=0)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_label = Label(editor, text='Zip Code:')
    zipcode_label.grid(row=5, column=0)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # create or connect a database
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    # Query the database
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create a save button
    edit_btn = Button(editor, text='Save Records', command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

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

delete_box_label = Label(root, text='Select ID: ')
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

# create an update button
edit_btn = Button(root, text='Update Records', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

conn.commit()
conn.close()

root.mainloop()