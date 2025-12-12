# Basic file opening
file = open('file.txt', 'r')  # 'r' = read mode
content = file.read()
file.close()

# Better practice: using 'with' (auto-closes)
with open('file.txt', 'r') as file:
    content = file.read()
    
    
# Read entire file
with open('data.txt', 'r') as file:
    all_content = file.read()

# Read line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read lines into list
with open('data.txt', 'r') as file:
    lines = file.readlines()
    
    
    
# Write new file (overwrites existing)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Append to existing file
with open('output.txt', 'a') as file:
    file.write("This line is appended\n")