import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')
conn.commit()

# Insert data
cursor.execute('''
    INSERT INTO students (name, age, email)
    VALUES (?, ?, ?)
''', ('John Doe', 20, 'john@email.com'))
conn.commit()


cursor.execute('''
    UPDATE students
    SET age = ?
    WHERE id = ?
''', (21, 1))
conn.commit()
# Delete specific record
cursor.execute("DELETE FROM students WHERE id = ?", (1,))
conn.commit()

# Delete all records
cursor.execute("DELETE FROM students")
conn.commit()