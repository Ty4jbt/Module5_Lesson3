# Import the connect_database function from the connect_mysql module
from connect_mysql import connect_database

# Establish a connection to the database
conn = connect_database()

if conn is not None:
    try:
        cursor = conn.cursor()
        
        # Query to fetch orders by customers whose name starts with 'John'
        query = """
        SELECT o.id AS OrderID, o.date AS OrderDate, c.id AS CustomerID, c.name, c.email
        FROM Customers c, Orders o
        WHERE c.id = o.customer_id AND c.name LIKE 'John%'
        """
        
        cursor.execute(query)
        
        # Fetching all the rows from the result set
        for order in cursor.fetchall():
            print(order)

    # Handling exceptions
    except Exception as e:
        print(f"Error: {e}")
        
    # Closing the connection to the database
    finally:
        cursor.close()
        conn.close()
        print("Connection to the database is closed.")