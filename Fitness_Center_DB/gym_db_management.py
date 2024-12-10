
# Establishing the connection to the database

import mysql.connector
from mysql.connector import Error

def connect_database():
    # Database connection parameters
    db_name = 'fitness_center_db'
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

# Gym Database Management
# Task 1: Add a new member to the gym database

def add_member(conn, id, name, age):

    try:
        cursor = conn.cursor()

        # Check if member already exists
        check_query = "SELECT * FROM Members WHERE id = %s"

        # Execute the query and requires an tuple as an argument
        cursor.execute(check_query, (id,))

        # Fetch the result and prints a message if the member already exists
        if cursor.fetchone():
            print(f"Member with ID {id} already exists.")
            return
        
        # Query to insert a new member into the database
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

        cursor.execute(query, (id, name, age))

        conn.commit()

        print(f"New member {name} added successfully.")

    # Handling exceptions
    except Error as e:
        print(f"Error while adding a new member: {e}")
        conn.rollback()

    # close the cursor
    finally:
        cursor.close()

# Task 2: Add a workout session for a member

def add_workout_session(conn, member_id, date, duration_minutes, calories_burned):

    cursor = None

    try:
        cursor = conn.cursor()

        # Check if member exists
        check_query = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(check_query, (member_id,))

        # If member does not exist, print a message and return
        if not cursor.fetchone():
            print(f"Member with ID {member_id} does not exist.")
            return

        # Insert the workout session into the database
        query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        
        cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
        
        conn.commit()
        
        print(f"Workout session added for member ID {member_id}.")
    
    # Handling exceptions
    except Error as e:
        print(f"Error adding workout session: {e}")

        if conn.is_connected():
            conn.rollback()
    
    # close the cursor
    finally:
        if cursor:
            cursor.close()

# Task 3: Update Member's Age

def update_member_age(conn, member_id, new_age):

    try:
        cursor = conn.cursor()

        # Check if member exists
        check_query = "SELECT * FROM Members WHERE id = %s"

        cursor.execute(check_query, ( member_id,))

        # If member does exist, update the age and commit the transaction
        if cursor.fetchone():
            update_query = "UPDATE Members SET age = %s WHERE id = %s"

            cursor.execute(update_query, (new_age, member_id))

            conn.commit()

            print(f"Member's age updated successfully.") 

    # Handling exceptions
    except Error as e:
        print(f"Error updating member's age: {e}")

    # close the cursor
    finally:
        cursor.close()


# Task 4: Delete a  workout session from the gym database

def delete_workout_session(conn, session_id):

    try:
        cursor = conn.cursor()

        check_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"

        cursor.execute(check_query, (session_id,))

        # If the workout session exists, delete it and commit the transaction
        if cursor.fetchone():
            delete_query = "DELETE FROM WorkoutSessions WHERE member_id = %s AND date = %s"

            cursor.execute(delete_query, (session_id,))

            conn.commit()

            print(f"Workout session with ID {session_id} deleted.")

        # If the workout session does not exist, print a message
        else:
            print(f"No workout session with ID {session_id} not found.")

    # Handling exceptions
    except Error as e:
        print(f"Error deleting workout session: {e}")
        cursor.rollback()

    # close the cursor
    finally:
        cursor.close()

# Assignment 2
# Task 1: Retrieve members in a specific age range

def get_members_in_age_range(conn, start_age, end_age):
    try:
        cursor = conn.cursor(dictionary=True)

        # Uses the between operator to retrieve members in the specified age range
        query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
        
        cursor.execute(query, (start_age, end_age))
        
        members = cursor.fetchall()
        
        # Print the members in the specified age range
        if members:
            print(f"Members between {start_age} and {end_age} years old:")
        
            for member in members:
                print(f"ID: {member['id']}, Name: {member['name']}, Age: {member['age']}")
        
        else:
            print(f"No members found between {start_age} and {end_age} years old.")
        
        return members
    
    # Handling exceptions
    except Error as e:
        print(f"Error retrieving members in age range: {e}")
        return None
    
    # close the cursor
    finally:
        cursor.close()

# Main execution
if __name__ == "__main__":
    conn = connect_database()
    
    if conn:
        try:
            # Example usage of functions
            add_member(conn, 1, "John Doe", 28)
            add_workout_session(conn, 1, "2024-12-04", 60, 300)
            update_member_age(conn, 1, 29)
            delete_workout_session(conn, 1)
            get_members_in_age_range(conn, 25, 30)
    
        # Makes sure the connection is closed
        finally:
            if conn.is_connected():
                conn.close()
                print("Database connection closed.")