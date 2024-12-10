# Importing the connect_database function from the connect_mysql file
from connect_mysql import connect_database

# Establishing a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()

        # Customer details to be removed
        customer_to_remove = (1, )

        query_check = "SELECT * FROM Orders WHERE customer_id = %s"
        cursor.execute(query_check, customer_to_remove)

        orders = cursor.fetchall()

        # Check if the customer has any orders
        if orders:
            print("Cannot remove customer as they have orders.")
        else:
            query = "DELETE FROM Customers WHERE id = %s"

            cursor.execute(query, customer_to_remove)

            conn.commit()

            print("Customer removed successfully.")

    # Handling exceptions
    except Exception as e:
        print(f"Error: {e}")

    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")