
text = "One of the student came with an hp laptop and handed it over to me"
#replace one of the student with "Ade"
new_text = text.replace("One of the student", "Ade")
print(new_text)

position = text.find("of")

print(position)

from datetime import datetime

time =datetime.now()

person = "Ade"

print(f'I am already here with {person} at {time}') 

difference = len(new_text) - len(text)
difference = abs(difference)

print(difference)

nums = [3, 1, 2]
print( f'nums {nums}')
nums.append(4)          # [3,1,2,4]
print(f'append nums {nums}')
nums.extend([5,6])      # [3,1,2,4,5,6]
print(f'extend nums {nums}')
nums.insert(1, 10)      # [3,10,1,2,4,5,6]
print(f'insert nums {nums}')
nums.remove(2)          # [3,10,1,4,5,6]
print(f'remove nums {nums}')
print(nums.pop())       # 6, nums = [3,10,1,4,5]
print(f'pop nums {nums}')
print(nums.index(10))   # 1
print(f'index of 10 {nums}')
print(nums.count(4))    # 1
print(f'count of 4 {nums}')
nums.sort()             # [1,3,4,5,10]
print(f'sort {nums}')
nums.reverse()          # [10,5,4,3,1]
print(f'reverse nums {nums}')
nums_copy = nums.copy() # [10,5,4,3,1]
print(f'copy list to nums_copy {nums_copy}')
nums.clear()            # []
print(f'clear nums {nums}')