import psycopg2

#Establishing the connection
conn = psycopg2.connect(
        user='sales_admin',
        password="sales_management",
        host="localhost",
        port="5432",
        database="gui_project"
    )
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO women(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Mayowa', 'Akinade', 34, 'M', 9000)''')
cursor.execute('''INSERT INTO women(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Esther', 'Akinyanmi', 20, 'F', 6000)''')
cursor.execute('''INSERT INTO women(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO women(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO women(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()