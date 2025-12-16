import sqlite3

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER,
    class_name TEXT,
    department TEXT
)
""")

conn.commit()
conn.close()


# ---------- DATA MODEL ----------
class Student:
    def __init__(self, full_name, age, class_name, department):
        self.full_name = full_name
        self.age = age
        self.class_name = class_name
        self.department = department

    def __str__(self):
        return f"{self.full_name} | {self.age} | {self.class_name} | {self.department}"


# ---------- CRUD FUNCTIONS ----------
def add_student(student):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (full_name, age, class_name, department)
    VALUES (?, ?, ?, ?)
    """, (student.full_name, student.age, student.class_name, student.department))

    conn.commit()
    conn.close()


def view_students():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_student(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()
    return student


def update_student_class(student_id, new_class):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET class_name = ?
    WHERE id = ?
    """, (new_class, student_id))

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()


# ---------- CONSOLE APP ----------
while True:
    print("\n--- SCHOOL MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Class")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Select option: ")

    if choice == "1":
        name = input("Full Name: ")
        age = int(input("Age: "))
        class_name = input("Class (e.g. JSS1): ")
        dept = input("Department: ")

        student = Student(name, age, class_name, dept)
        add_student(student)
        print("Student added successfully")

    elif choice == "2":
        students = view_students()
        for s in students:
            print(s)

    elif choice == "3":
        sid = int(input("Student ID: "))

        student = get_student(sid)
        if student is None:
            print("Student not found")
        else:
            print("Current Record:", student)
            new_class = input("New Class: ")
            update_student_class(sid, new_class)
            print("Student class updated")

    elif choice == "4":
        sid = int(input("Student ID: "))

        student = get_student(sid)
        if student is None:
            print("Student not found")
        else:
            print("Student Record:", student)
            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":
                delete_student(sid)
                print("Student deleted")
            else:
                print("Delete cancelled")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid option")
