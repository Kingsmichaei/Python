"""
FILE HANDLING + ERROR HANDLING EXAMPLE
---------------------------------------
This file teaches:
1. Creating and writing to a file
2. Reading a file
3. Appending to a file
4. Using try/except to handle errors
"""

def write_file(filename, content):
    """Create a file or overwrite if it exists."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print("File written successfully!")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print("Unexpected error:", e)


def read_file(filename):
    """Read a file safely."""
    try:
        with open(filename, 'r') as f:
            data = f.read()
        print("File content:\n", data)
    except FileNotFoundError:
        print("Error: File not found. Make sure the file exists.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print("Unexpected error:", e)


def append_file(filename, new_text):
    """Append text to an existing file."""
    try:
        with open(filename, 'a') as f:
            f.write("\n" + new_text)
        print("Text appended successfully!")
    except FileNotFoundError:
        print("Error: Cannot append. File does not exist.")
    except Exception as e:
        print("Unexpected error:", e)


def safe_division(a, b):
    """Practice error handling with numbers."""
    try:
        result = a / b
        print("Result =", result)
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    except TypeError:
        print("Error: Please enter numbers only!")
    except Exception as e:
        print("Unexpected error:", e)

filename = "students.txt"

# 1. Write to file
write_file(filename, "Name: John Doe\nScore: 85")

# 2. Read file
read_file(filename)

# 3. Append new data
append_file(filename, "Name: Jane Doe\nScore: 90")

# 4. Read again
read_file(filename)

# 5. Error handling demonstration
safe_division(10, 0)  # ZeroDivisionError example
safe_division("a", 5)  # TypeError example
