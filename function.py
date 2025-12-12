from datetime import datetime
import math
import random

def square(n):
    return n * n


square_number = square(5)


print(square_number)

print(square(4))

print(square(6))

def say_hello():
    print("Hello, welcome to Python functions!")

say_hello()

numbers = [1, 2, 3, 4, 5, 6 ]
def get_even(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result

print(get_even(numbers))

items = ['apple', 'banana', 'grape']
def print_list(items):
    for item in items:
        print("Item:", item)

print_list(items)

def circle_area(radius):
    return math.pi * radius * radius

print("Area of a circle (r=5):", circle_area(5))

items = ['apple', 'banana', 'grape']
def random_choice(items):
    return random.choice(items)

randomItem = random_choice(items)
print("Random color:", randomItem)


#date and time module
def how_many_days_ago(year, month, day):
    past_date = datetime.date(year, month, day)
    current_date = datetime.date.today()
    delta = current_date - past_date
    return delta.days

#function with dictionary parameter
def print_person_info(person):
    for key, value in person.items():
        print(f"{key}: {value}")
        