from crud.insert import create_user
from crud.read import read_users
from crud.update import update_user
from crud.delete import delete_user
from crud.create_table import create_users_table


def menu():
    while True:
        print("\n===== PostgreSQL CRUD Menu =====")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            create_user(username)

        elif choice == "2":
            read_users()

        elif choice == "3":
            try:
                user_id = int(input("Enter user ID: "))
                username = input("Enter new username: ")
                update_user(user_id, username)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    create_users_table()
    menu()