import psycopg2

from psycopg2 import Error

try:
    # connect to an existing database
    connection = psycopg2.connect(
        user='sales_admin',
        password="sales_management",
        host="localhost",
        port="5432",
        database="gui_project"
    )
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    print('PostgreSQL server information:')
    print(connection.get_dsn_parameters(), '\n')
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print('You are connected to - ', record, '\n')

except (Exception, Error) as error:
    print('Errorn while connecting to PostgreSQL', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')
