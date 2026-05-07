'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr and Argument
(3) Keyword & default Argument
(4) Scope
'''

print("===== DEFINE vs CALL =====")
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
