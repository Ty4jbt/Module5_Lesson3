# Importing the connect_database function from the connect_mysql.py file
from connect_mysql import connect_database

# Establishing a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        query = "SELECT * FROM customers"

        cursor.execute(query)
        
        # Fetching all the rows from the result set
        for row in cursor.fetchall():
            print(row)

    # Handling exceptions
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")