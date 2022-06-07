import sqlite3


def employee_table():
    conn = sqlite3.connect('projects/employee.db')
    print('database employee.db created!!!')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee_table (id INTEGER PRIMARY KEY, department text, name text, \
                    designation text, email text, address text, marital_status text, date_of_birth text, date_joined text, id_type text,\
                    id_value text, gender text, phone text, country text, salary text)"
                   )
    conn.commit()
    print('employee_table created!!!')
    conn.close()


def employee_data(dep, name, designation, email, address, married, dob, doj, idproofcomb, idproof, gender, phone, country, salary):
    conn = sqlite3.connect('projects/employee.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employee_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        dep, name, designation, email, address, married, dob, doj, idproofcomb, idproof, gender, phone, country, salary
    ))
    conn.commit()
    print('employee data added!!!')
    conn.close()