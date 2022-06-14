from tkinter import *
import sqlite3


root = Tk()
root.title('Affable Digital Services')
root.geometry('400x400')

# create or connect a database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# create table
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


conn.commit()
conn.close()

root.mainloop()