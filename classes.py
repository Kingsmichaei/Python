


class Person:
    def __init__(self, name, age):
        # Attributes
        self.name = name
        self.age = age
        print(f"Person {self.name} created.")

    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

    def present(self):
        print(f"My name is {self.name}.")


# p1 = Person("John", 25)

# p2 = Person("Mary", 30)
# print(p1.greet())
# print(p2.greet())


# 2. CLASS WITH METHODS
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance


# Usage
a = BankAccount("Seun", 1000)
print(a.deposit(500))
print(a.withdraw(300))


class Book:
    def __init__(self, no_pages):
        self.no_pages = no_pages

    def info(self):
        return f"Number of pages: {self.no_pages}"


class SubjectBook(Book):
    def __init__(self, no_pages, subject, topic):
        super().__init__(no_pages)
        self.subject = subject
        self.topic = topic

    def details(self):
        return (
            f"Subject: {self.subject}\n"
            f"Topic: {self.topic}\n"
            f"Pages: {self.no_pages}"
        )


# Example usage
book1 = SubjectBook(250, "Mathematics", "Algebra")
print(book1.details())
print(book1.info())


# 4. CLASS METHOD & STATIC METHOD
class MathTools:
    count = 0  # Class attribute

    def __init__(self):
        MathTools.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def add(a, b):
        return a + b


# Usage
m1 = MathTools()
m2 = MathTools()
MathTools()

print(MathTools.get_count())
print(MathTools.add(10, 5))


# 5. ENCAPSULATION (PRIVATE VARIABLES)
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # private attribute

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if value >= 0:
            self.__score = value
        else:
            print("Invalid score")


s = Student("Tolu", 85)
print(s.get_score())
s.set_score(95)
print(s.get_score())


# 6. PRACTICAL REAL WORLD PROJECT EXAMPLE
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def full_name(self):
        return f"{self.year} {self.brand} {self.model}"


car1 = Car("Toyota", "Camry", 2020)
print(car1.full_name())


# END OF FILE

# POLYMORPHISM EXAMPLE


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound"


class Dog(Animal):  # Inheritance
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


class PythonClass():
    def __init__(self, results=None):
        self.no_student = len(results) 
        self.results = results

    def print_no_student(self):
        print(f"Number of students in Python class: {self.no_student}")

    def print_results(self):
        if self.results:
            for student, score in self.results.items():
                print(f"{student}: {score}")
        else:
            print("No results available.")


class DesignClass():
    def __init__(self, results=None):
        self.no_student = len(results) 
        self.results = results

    def print_no_student(self):
        print(f"Number of students in Design class: {self.no_student}")

    def print_results(self):
        if self.results:
            for student, score in self.results.items():
                print(f"{student}: {score}")
        else:
            print("No results available.")


class CyberSecurityClass():
    def __init__(self, results=None):
        self.no_student = len(results) 
        self.results = results

    def print_no_student(self):
        print(f"Number of students in Cyber Security class: {self.no_student}")

    def print_results(self):
        if self.results:
            for student, score in self.results.items():
                print(f"{student}: {score}")
        else:
            print("No results available.")



pythonClassResult = {"Ade": 85, "Bola": 90, "Chinedu": 78, "Dayo": 88, "Eunice": 92}
designClassResult = {"Efe": 88, "Funmi": 92, "Goke": 80, "Hauwa": 85}
cyberSecurityClassResult = {"Hakeem": 95, "Ije": 89, "Jide": 78, "Kemi": 84, "Leke": 91, "Mide": 87}

HiiTClass = [PythonClass( pythonClassResult), DesignClass( designClassResult), CyberSecurityClass( cyberSecurityClassResult)]

for students in HiiTClass:
    # students.print_no_student()
    print(students.no_student)
    print(students.results)
    


class Tailor():
    def __init__(self):
        self.shared_materials = ["measuring tape", "scissors", "needles", "threads"]
        self.__personal_tools = ["sewing machine", "iron", "cutting table"]
        
        def book_slot(self, date, time):
            return f"Tailoring slot booked for {date} at {time}."
        
        def __free_slot(self):
            print("Family and friends only.")
            
            
myTailor = Tailor()
print(myTailor.shared_materials)
print(myTailor.__personal_tools)  # This will raise an AttributeError