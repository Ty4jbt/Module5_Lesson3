# Import the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establish a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()

        # Updated customer details
        updated_customer = ("Hilary Boe", "hilary.boe@gmail.com", 6)
        
        query = "UPDATE Customers SET name = %s, email = %s WHERE id = %s"

        cursor.execute(query, updated_customer)
        
        conn.commit()
        
        print("Customer updated successfully.")

    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")