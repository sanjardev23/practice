''' LOOPS operators
    (1) for
    (2) break/else
    (3) while  
'''

print("====== for operator ======")
# for is used to iterate over a sequence (like a list, tuple, string, etc.) or other iterable objects.
# Iterable objects > stirng dict tuple list range map filter
text = "MIT"
nums = [1, 2, 3, 4, 5]
car_obj = dict(brand="CLS 63s", year=2026)
range_obj = range(5)


for letter in text:
    print(f"the letter is: {letter}")

print("-"*10)
for number in nums:
    print(f"the number is: {number}")

print("-"*10)
for x in range_obj:
    print(f"the element is: {x}")

print("-"*10)
for key in car_obj:
    print(f"the key is: {key} and the value is: {car_obj[key]}")

print("-"*10)
for x in range(1, 20, 5):
    print(f"the element x is: {x}")




print("====== break/else operator ======")
# break is used to exit a loop prematurely when a certain condition is met.
for x in range(1, 20, 5):
    print(f"the element x is: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Executed successfully without break")
    
    
    

print("====== while operator ======")
# while is used when we want to repeat a block of code until a certain condition is met.
number = 40
while number > 0:
    number -= 10 
    print(f"the number is: {number}")
    
    
print("-"*10)
count = 0
while True:
    count += 1
    x = int(input("Find a number: "))
    
    if x == 41:
        print(f"Congratulations! You found the number in {count} attempts.")
        break
    else:
        print("Try again!")