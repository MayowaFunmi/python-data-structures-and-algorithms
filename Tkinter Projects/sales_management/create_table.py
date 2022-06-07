import psycopg2

#Establishing the connection
conn = psycopg2.connect(
        user='sales_admin',
        password="sales_management",
        host="localhost",
        port="5432",
        database="gui_project"
    )


#Creating a cursor object using the cursor() method
cursor = conn.cursor()


#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS women")


#Creating table as per requirement
sql ='''CREATE TABLE women(
   FIRST_NAME CHAR(25) NOT NULL,
   LAST_NAME CHAR(25),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()