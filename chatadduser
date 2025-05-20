#!/usr/bin/env python3
import bcrypt
import json
import os
from getpass import getpass

USERS_FILE = "chat_users.json"

def add_user(username, password):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
    else:
        users = {}

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = hashed

    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

    print(f"User {username} added.")

def delete_user(username):
    if not os.path.exists(USERS_FILE):
        print("User database not found.")
        return

    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    if username in users:
        del users[username]
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        print(f"User {username} deleted.")
    else:
        print(f"User {username} not found.")

def change_password(username, new_password):
    if not os.path.exists(USERS_FILE):
        print("User database not found.")
        return

    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    if username in users:
        hashed = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
        users[username] = hashed
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f, indent=2)
        print(f"Password for user {username} changed.")
    else:
        print(f"User {username} not found.")

def get_password_with_confirmation(prompt="Enter password: "):
    while True:
        p1 = getpass(prompt)
        p2 = getpass("Confirm password: ")
        if p1 != p2:
            print("Passwords do not match, try again.")
            continue
        return p1

def authenticate_admin():
    if not os.path.exists(USERS_FILE):
        print("User database not found.")
        return False

    with open(USERS_FILE, 'r') as f:
        users = json.load(f)

    admin_user = input("Admin username: ").strip()
    if admin_user not in users:
        print("Admin user not found.")
        return False

    admin_pass = getpass("Admin password: ")
    hashed = users[admin_user]

    if bcrypt.checkpw(admin_pass.encode(), hashed.encode()):
        return True
    else:
        print("Invalid admin password.")
        return False

def main():
    choice = input("Choose an action: [add/delete/change_password]: ").strip().lower()
    if choice == "add":
        u = input("Enter new username: ").strip()
        p = get_password_with_confirmation()
        add_user(u, p)
    elif choice == "delete":
        if authenticate_admin():
            u = input("Enter username to delete: ").strip()
            delete_user(u)
        else:
            print("Admin authentication failed. Cannot delete user.")
    elif choice == "change_password":
        u = input("Enter username to change password: ").strip()

        # New: verify old password before changing
        if not os.path.exists(USERS_FILE):
            print("User database not found.")
            return

        with open(USERS_FILE, 'r') as f:
            users = json.load(f)

        if u not in users:
            print(f"User {u} not found.")
            return

        old_pass = getpass("Enter current password: ")
        hashed = users[u]

        if not bcrypt.checkpw(old_pass.encode(), hashed.encode()):
            print("Current password incorrect. Password not changed.")
            return

        p = get_password_with_confirmation("Enter new password: ")
        change_password(u, p)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
