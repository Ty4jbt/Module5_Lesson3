
# Establishing the connection to the database

import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = 'e_commerce_db'
    user = 'root'
    password = 'Full-Stack-dev97'
    host = '127.0.0.1'

    # Establishing the connection
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        # Checking if the connection is successful
        print("Connection to the database is successful.")
        return conn

    # Handling exceptions
    except Error as e:
        print(f"Error while connecting to the database: {e}")
        return None