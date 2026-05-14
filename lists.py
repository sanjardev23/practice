'''List
(1) Working with list
(2) List methods
(3) Lambda functions
(4) enumarate, mao and filter
'''

print("======= LISTS =======")
# Java/ PHP/ JS > Array => Python List


# literal
person = {"name": "Alice", "age": 30, "single": True}    # thi is a dict,
people = ("Alice", "Bob", "Charlie")                    # this is a tuple,
groups = ["MIT", "FLEXY", "DEVEX", "MG"]              # this is a list,
for team in groups:
    print(f"the team: {team}")


# constructor
result = list("Hello world")                            # this is a list
print(f"letters: {result} and size of letters: {len(result)}")


print("-"*10)
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]

# gives us the first and the last fruit, because we are skipping 3 elements
c = fruits[::3]
d = fruits[-1]          # gives us the last fruit


print(f"the first fruit: {a}")
print(f"the first two fruits: {b}")
print(f"the first and the last fruit: {c}")
print(f"the last fruit: {d}")






print("====== List methods ======")
# methods > append() insert() pop() remove() clear() sort() reverse() count() index()

letters = ["a", "b", "c", "d"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert letters: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")

print("------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear:", animals)


if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist in animals list")


print("-"*10)
numbers = [1, 5, 3, 2, 4]
numbers.sort()                # sort in ascending order
print("sort default:", numbers)
numbers.sort(reverse=True)    # sort in descending order
print("sort reverse:", numbers)


# immutable > sorted function & index() method
numbs = [5, 2, 4, 1, 3]
new_numbs = sorted(numbs)      # sort in ascending order
print(f"the sorted numbs: {numbs} and  new_numbs: {new_numbs}")





