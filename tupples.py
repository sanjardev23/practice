''' TUPLES
    (1) What is a tuple: tuple & list
    (2) Unpacking arguments
    (3) zip
'''

print("======= TUPLES =======")
# Jva/PHP/NodeJS > array => Python list, array





# literal
nums = [3, 5, 1, 2, 4]
print(nums)
# car_dict = {"brand": "BMW", "model": "X5", "year": 2020} # thi is a dict, made in literal way

# constructor
letters = list("Helo world")
print(letters)
# person_dict = dict(name="Alice", age=30) # this is a dict, made in constructor way


fruits = ["apple", "banana", "cherry"]     # this is a list, made in literal way
print("before fruits:", fruits)

fruits[2] = "melon"                        # this is a list, mutable, we can change the value of an element
print("after fruits:", fruits)


animal_tuple = ("cat", "dog", "rabbit")         # this is a tuple, made in literal way
tupple_obj = ("MIT", 100, True, None)          # this is a tuple, made in literal way, we can put different types of data in a tuple

print(animal_tuple[0])
# animal_tuple[0] = "hamster"                      # this will raise an error, because tuple is immutable, we cannot change the value of an element


# try avoid this
people = "Alice", "Bob"
animals = "cat", "dog", "rabbit"





print("======= UNPACKING ARGUMENTS =======")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"x: {x}, y: {y}, z: {z}")
print("z:", z)


# *args > tuple
def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total

# call
calculate(1, 7, 2, 3)
print("-"*10)
calculate(0, 2, 300)
print("-"*10)
calculate(5, 7)


