# int
x = 10
print(x.bit_length())   # 4 -> bits to represent 10
print(x.to_bytes(2, 'big'))  # b'\x00\n'
print(int.from_bytes(b'\x00\n', 'big'))  # 10

# float
y = 3.14159
print(round(y, 2))  # 3.14
print(abs(-5.5))    # 5.5
print(divmod(10, 3)) # (3, 1)


#String
text = " hello World "

print(text.upper())       # " HELLO WORLD"
print(text.lower())       # " hello world"
print(text.title())       # " Hello World"
print(text.capitalize())  # " Hello world"
print(text.strip())       # "hello World"
print(text.lstrip())      # "hello World "
print(text.rstrip())      # " hello World"
print(text.replace("World","Python"))  # " hello Python "
print(text.split())       # ['hello', 'World']
print(" ".join(["a","b","c"]))  # "a b c"
print(text.find("World")) # 7
print(text.count("l"))    # 3
print(text.startswith(" ")) # True
print(text.endswith("d "))   # True
print("abc123".isalnum())    # True
print("abc".isalpha())       # True
print("123".isdigit())       # True


#List   
nums = [3, 1, 2]
nums.append(4)          # [3,1,2,4]
nums.extend([5,6])      # [3,1,2,4,5,6]
nums.insert(1, 10)      # [3,10,1,2,4,5,6]
nums.remove(2)          # [3,10,1,4,5,6]
print(nums.pop())       # 6, nums = [3,10,1,4,5]
print(nums.index(10))   # 1
print(nums.count(4))    # 1
nums.sort()             # [1,3,4,5,10]
nums.reverse()          # [10,5,4,3,1]
nums_copy = nums.copy() # [10,5,4,3,1]
nums.clear()            # []

#Tuple
t = (1,2,3,2)
print(t.count(2))  # 2
print(t.index(3))  # 2


#Dictionary
person = {"name":"John","age":30}

print(person.keys())        # dict_keys(['name','age'])
print(person.values())      # dict_values(['John',30])
print(person.items())       # dict_items([('name','John'),('age',30)])
print(person.get("age"))    # 30
person.update({"job":"Dev"})
print(person)               # {'name': 'John', 'age': 30, 'job': 'Dev'}
print(person.pop("age"))    # 30, person = {'name': 'John','job':'Dev'}
print(person.popitem())     # Removes last inserted, e.g., ('job','Dev')
person.setdefault("country","USA") # Adds key if missing
person_copy = person.copy() # Shallow copy
person.clear()              # {}


#Set
a = {1,2,3}
b = {3,4,5}

a.add(6)                   # {1,2,3,6}
a.update([7,8])            # {1,2,3,6,7,8}
a.remove(2)                # {1,3,6,7,8}
a.discard(100)             # no error
print(a.pop())             # Removes random element
print(a.union(b))          # {1,2,3,4,5,6,7,8}
print(a.intersection(b))   # {3}
print(a.difference(b))     # {1,6,7,8}
print(a.symmetric_difference(b)) # {1,4,5,6,7,8}
a_copy = a.copy()          # shallow copy
a.clear()                  # {}


#Frozenset
fs = frozenset([1,2,3])
print(fs.union({3,4}))           # {1,2,3,4}
print(fs.intersection({2,3,5}))  # {2,3}
print(fs.difference({2}))        # {1,3}
print(fs.symmetric_difference({3,4})) # {1,2,4}
fs_copy = fs.copy()              # frozenset({1,2,3})


#Boolean
a = True
b = False
print(a and b)   # False
print(a or b)    # True
print(not a)     # False
print(bool(0))   # False
print(bool(1))   # True
