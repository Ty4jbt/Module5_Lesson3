# Importing the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establishing a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        # Order details to be deleted
        customer_id = 5
        order_id = 2
        
        query = "DELETE FROM Orders WHERE id = %s and customer_id = %s"
        
        cursor.execute(query, (order_id, customer_id))
        
        conn.commit()
        
        print("Order deleted successfully.")
        
    # Handling exceptions
    except Exception as e:
        print(f"Error: {e}")
        
    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")