# crud/read.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection


def read_users():
    conn = get_db_connection()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users;"
            cursor.execute(query)

            users = cursor.fetchall()

            if users:
                print("Users:")
                for user in users:
                    print(f"ID: {user[0]}, Username: {user[1]}")
            else:
                print("No users found.")

            cursor.close()

        except Exception as e:
            print(f"Error reading users: {e}")

        finally:
            conn.close()


if __name__ == "__main__":
    read_users()