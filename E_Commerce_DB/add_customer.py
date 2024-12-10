# Imports the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establishes a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        # New customer details
        new_customer = ("Tyler Boe", "tyler.boe@gmail.com", "123-456-7890")

        # Query to insert a new customer into the database
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        cursor.execute(query, new_customer)

        conn.commit()

        print("New customer added successfully.")

    # Closes the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")

