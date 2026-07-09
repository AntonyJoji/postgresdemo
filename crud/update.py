# crud/update.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import get_db_connection


def update_user(user_id, new_username):
    conn = get_db_connection()

    if conn:
        try:
            cursor = conn.cursor()

            query = """
            UPDATE users
            SET username = %s
            WHERE id = %s;
            """

            cursor.execute(query, (new_username, user_id))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"User with ID {user_id} updated successfully.")
            else:
                print(f"No user found with ID {user_id}.")

            cursor.close()

        except Exception as e:
            print(f"Error updating user: {e}")

        finally:
            conn.close()


# Example
update_user(2, "arun")