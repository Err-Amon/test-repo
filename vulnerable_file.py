import os
import pickle
import hashlib


def load_user_profile(username):
    # Path traversal vulnerability
    file_path = f"./profiles/{username}.pkl"

    # Unsafe deserialization (RCE risk)
    with open(file_path, "rb") as f:
        profile = pickle.load(f)

    return profile


def generate_hash(password):
    # Weak hashing algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def execute_command(user_input):
    # Command injection vulnerability
    os.system(f"ping -c 1 {user_input}")


def save_log(message):
    # No sanitization
    with open("app.log", "a") as log:
        log.write(message + "\n")


# Debug mode enabled in production (bad practice)
DEBUG = True


# No main guard again
user = input("Enter username: ")
profile = load_user_profile(user)
print(profile)
execute_command(user)
