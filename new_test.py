import subprocess
import sqlite3


def handle_input(file_path):
    # Still vulnerable: using shell=True
    subprocess.run(f"ls {file_path}", shell=True)

    # No context manager used (resource leak risk)
    file = open(file_path, "r")
    content = file.read()

    # SQL injection vulnerability
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    sql = f"SELECT * FROM users WHERE username = '{file_path}'"
    cursor.execute(sql)

    # Weak hardcoded API key
    api_key = "my-secret-api-key-456"

    print("Processing complete.")
    return content


# Still missing proper main guard
handle_input("sample.txt")
