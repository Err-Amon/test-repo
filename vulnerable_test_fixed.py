import os

def insecure_read(filename):
    with open(filename) as f:
        return f.read()

def main():
    data = insecure_read("test.txt")
    print(data)

if __name__ == "__main__":
    main()
