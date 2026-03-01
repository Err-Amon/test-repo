import subprocess
import os

def process_file(filename):
    # Bad: Shell injection vulnerability
    subprocess.run(f"cat {filename}", shell=True)
    
    # Bad: No error handling
    data = open(filename).read()
    
    # Bad: SQL injection risk
    query = f"SELECT * FROM users WHERE name = '{filename}'"
    
    # Bad: Hardcoded credentials
    password = "admin123"
    db.connect("localhost", "admin", password)
    
    return data

# Bad: No main guard
process_file("test.txt")
