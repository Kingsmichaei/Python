try:
    # Risky code
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Something went wrong: {e}")
    
try:
    file = open('nonexistent.txt', 'r')
    content = file.read()
    number = int(content)
    result = 100 / number
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("File doesn't contain a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
else:
    print(f"Success! Result: {result}")
finally:
    print("This always runs")
    if 'file' in locals() and not file.closed:
        file.close()
        
        
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("Must be 18 or older!")
    return True

# Using the function
try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")