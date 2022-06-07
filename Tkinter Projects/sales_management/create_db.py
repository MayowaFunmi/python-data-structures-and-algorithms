import psycopg2

# first connect to postgres database
connection = psycopg2.connect(
        user='postgres',
        password="Treasure@1",
        host="localhost",
        port="5432",
        database="postgres"
    )
connection.autocommit = True
cursor = connection.cursor()
# create new database
cursor.execute('''CREATE DATABASE gui_project;''')
cursor.execute('''CREATE USER sales_admin WITH ENCRYPTED PASSWORD 'sales_management';''')
cursor.execute('''ALTER ROLE sales_admin SET client_encoding TO 'utf8';''')
cursor.execute('''ALTER ROLE sales_admin SET default_transaction_isolation TO 'read committed';''')
cursor.execute('''ALTER ROLE sales_admin SET timezone TO 'Africa/Lagos';''')
cursor.execute('''GRANT ALL PRIVILEGES ON DATABASE gui_project TO sales_admin;;''')
print("Database created successfully........")

connection.close()
