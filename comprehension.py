''' Comprehension
    (1) What is comprehension & list comp.
    (2) set and dictionary comp.
'''
# Comprehension -> loopni short yozish usuli



print("===== What is comprehension & list comprehenion ======")
# comprehension acts like spread operator


# comprehension yozish formati
''' Comprehension general syntax:     
    a) *iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>

'''

# list comp.
numbers = [1, 2, 3, 4, 2, 1, 20]
list_numbers = [*numbers]     # a version -> listni copy qilish

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


print("-"*10)
people = [("Robert", 21), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0]for person in people]    # b version -> list ichida tuple
print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]

# c version -> filter + loop birga ishlagan comprehension
list_cars = [car[0] for car in cars if car[1] > 80]
print("list_cars:", list_cars)






print("===== set and dictionary comp. ======")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}     # setni ichida order mavjud emas
print("set_numbs:", set_numbs)


dict_people = {person[0]: person[1] for person in people}    # b version
print("dict_people:", dict_people)

dict_people2 = {person[0]: person[1]for person in people if person[1] > 20}    # c version
print("dict_people2:", dict_people2)



# List comprehension  → []
# Set comprehension   → {} unique only
# Dict comprehension  → {key:value}

# Comprehension = for loopni short va smart yozish usul






# <expression> for item in iterable <condition>  -> generic