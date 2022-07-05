import sqlite3


def employee_table():
    conn = sqlite3.connect('projects/employee.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee_table (department text, name text, designation text, email text,\
                    address text, marital_status text, date_of_birth text, date_joined text, id_type text,\
                    id_value text, gender text, phone text, country text, salary text)"
                   )
    conn.commit()
    conn.close()


def employee_data(dep, name, designation, email, address, married, dob, doj, idproofcomb, idproof, gender, phone, country, salary):
    employee_table()
    conn = sqlite3.connect('projects/employee.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employee_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        dep, name, designation, email, address, married, dob, doj, idproofcomb, idproof, gender, phone, country, salary
    ))
    conn.commit()
    conn.close()


# function to change search type
def rename(option):
    lower = option.lower()
    c = lower.replace(' ', '_')
    return c
