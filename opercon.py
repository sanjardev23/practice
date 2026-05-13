''' OPERATORS & CONDITIONS
(1) Operators
(2) Conditions
(3) Logical operators
'''

print("==== Operators ====")
# Operators > + - > >= < <=  == * /    // % += **

a = 19
b = 5

print(a / b)
result1 = a // b
left = a % b
print(f"result1: {result1} and left: {left}")


# a = a + 100
a += 100
print("a:", a)

print("b*b:", b*b)
print("b*b*b:", b*b*b)


print("="*10)


c = dict(name="SIMON", age=23)
d = dict(name="SIMON", age=23)
e = c

print("c == d:", c == d)   # True.   only checks the values
# c va d ning memory addresslari har xil, e ning memory addressi c ga teng
print(id(c), id(d), id(e))

data = c is d
print("c is d:", data)   # False.   checks the memory address
print("c is e:", c is e)


print("==== Conditions ====")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("==== Logical operators ====")
age = 21

# person = None

# if age > 18:
#     person = "Adult"
# else:
#     person = "Child"


# Ternary operator > shartni if-else orqali qisqa yozish usuli
person = "Adult" if age > 18 else "minor"
print("person:", person)

print("-"*10)

is_student = True
is_admin = False
is_guest = True
is_parent = False


if not is_student:
    print("Welcome here, do you want to be student?")
elif is_admin:
    print("Please, go to the main office!")
elif is_guest or is_parent:
    print("Waiting room is in 1st floor")
else:
    print("other cases")