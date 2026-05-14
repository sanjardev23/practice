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


animal_tuple = ("cat", "dog", "rabbit")         # this is a tuple, made in literal way
tupple_obj = ("MIT", 100, True, None)          # this is a tuple, made in literal way, we can put different types of data in a tuple

print(animal_tuple[0])
# animal_tuple[0] = "hamster"                      # this will raise an error, because tuple is immutable, we cannot change the value of an element










