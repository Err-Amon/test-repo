# vulnerable_test5.py

import os
import pickle
import random
import sqlite3


# Hardcoded database credentials
DB_USER = "admin"
DB_PASSWORD = "supersecret123"


def load_user_file(filename):
    # Path traversal vulnerability
    filepath = f"./uploads/{filename}"
    with open(filepath, "rb") as f:
        return pickle.load(f)  # Insecure deserialization


def generate_reset_token():
    # Insecure random token generation
    return str(random.randint(100000, 999999))


def get_user(username):
    # SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def delete_file(filename):
    # Unsafe file deletion
    os.system(f"rm -rf {filename}")


def main():
    print(get_user("admin"))
    print(generate_reset_token())


if __name__ == "__main__":
    main()
