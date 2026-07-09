# crud/insert.py
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection

def create_user(username):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()

            query = "INSERT INTO users (username) VALUES (%s);"
            cursor.execute(query, (username,))

            conn.commit()
            print(f"User {username} created successfully.")

            cursor.close()

        except Exception as e:
            print(f"Error creating user: {e}")

        finally:
            conn.close()

# create_user("2,arun")