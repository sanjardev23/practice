'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr and Argument
(3) Keyword & default Argument
(4) Scope
'''

print("===== DEFINE (parametr) vs CALL (argument) =====")
# build in function > print() type()
# Function - reusable block of code
# Instead of block {} in JAVA, Python uses indentation!


# DEFINE - parametr (build)
def great(a):
    print(f"How do you do, {a}?")


def greeting(b):
    print("Greeting function is executed")
    return f"Hi {b}!"


# CALL - argument (execute)
result1 = great("SIMON")
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)


print("===== Keyword & default Argument =====")
# DEFINE


def give_greet(name, age = 22):       # bu yerda age default argument (parameterga oldindan value berib qo‘yish.)
    print("give_great is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
# keyword argumen - functionga value’ni parameter nomi bilan yuborish
result3 = give_greet(name="SIMON", age=23)
print("result3:", result3)


result4 = give_greet("John")
print("result4:", result4)
