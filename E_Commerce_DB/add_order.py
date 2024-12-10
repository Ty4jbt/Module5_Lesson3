# Importing the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establishing a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        # New order details
        customer_id = 5
        order_date = "2024-12-03"
        
        # Query to insert a new order into the database
        query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"
        
        cursor.execute(query, (order_date, customer_id))
        
        conn.commit()
        
        print("New order added successfully.")
        
    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")