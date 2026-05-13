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
print(id(c), id(d), id(e))  # c va d ning memory addresslari har xil, e ning memory addressi c ga teng   

data = c is d
print("c is d:", data)   # False.   checks the memory address
print("c is e:", c is e) 
