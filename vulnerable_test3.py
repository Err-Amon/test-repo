import os
import subprocess
import sqlite3
import requests

def process_file(filename):
    # Vulnerable: Shell injection
    subprocess.run(f"cat {filename}", shell=True)

    # Vulnerable: Reading file without error handling
    with open(filename) as f:
        data = f.read()

    # Vulnerable: SQL injection
    query = f"SELECT * FROM users WHERE username = '{filename}'"
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

    # Vulnerable: Hardcoded API token
    api_token = "12345-secret-token"
    headers = {"Authorization": f"Bearer {api_token}"}
    requests.get("https://example.com/data", headers=headers)

    return data

# Vulnerable: No main guard
process_file("test.txt")
