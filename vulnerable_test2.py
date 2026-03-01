# vulnerable_test2.py

import os
import sqlite3
import requests

# Bad: Hardcoded API key
API_KEY = "12345-SECRET-API-KEY"

def fetch_data(url):
    # Bad: No error handling
    response = requests.get(url)
    return response.text

def unsafe_file_write(filename, content):
    # Bad: Shell injection vulnerability
    os.system(f"echo {content} > {filename}")

def query_user_data(username):
    # Bad: SQL injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
    result = cursor.fetchall()
    conn.close()
    return result

# Bad: No main guard
print(fetch_data("http://example.com"))
unsafe_file_write("test.txt", "Hello World")
print(query_user_data("admin"))
