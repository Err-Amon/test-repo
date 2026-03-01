import tempfile
import requests
import os

API_TOKEN = "hardcoded-token-789"  # Bad: hardcoded secret

def download_file(url):
    # No input validation (SSR, XSS, or remote file issues possible)
    response = requests.get(url)
    # No error handling
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(response.content)
    temp_file.close()
    print(f"Downloaded file saved to {temp_file.name}")  # Bad: prints full path

    # Insecure file permission change
    os.chmod(temp_file.name, 0o777)

    return temp_file.name

def process_file(file_path):
    # No try/except, could crash if file missing
    with open(file_path, "r") as f:
        content = f.read()

    # Shell injection vulnerability
    os.system(f"echo {content}")

    return content

# No main guard
url_input = input("Enter file URL to download: ")
file_path = download_file(url_input)
process_file(file_path)
