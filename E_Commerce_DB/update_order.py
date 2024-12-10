# Importing the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establishing a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        # Order details to be updated
        customer_id = 5
        order_id = 2
        new_order_date = "2024-12-02"
        
        query = "UPDATE Orders SET date = %s WHERE id = %s and customer_id = %s"
        
        cursor.execute(query, (new_order_date, order_id, customer_id))
        
        conn.commit()
        
        print("Order updated successfully.")

    # Handling exceptions
    except Exception as e:
        print(f"Error: {e}")
        
    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")