''' Array & Set
(1) Array
(2) Set
(3) Specific operators with set
'''

# array - katta data bilan ishlatiladi, kichigi bn list ishlatiladi
# array ishlatish un import qilinadi
from array import array
print("===== Array ======")

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)


print("====== Set =======")
# { set } of unique collection without keeping order!
# setda index bolmaydi | order saqlamaydi | bir hil qiymat saqlamaydi
new_numbers = array("i", [1, 4, 5, 7, 8, 41])
number_set = set(new_numbers)

print(f"the number_set: {number_set} and type {type(number_set)}")

number_set.add(200)
print("number_set(1)", number_set)

number_set.add(7)
print("number_set(2)", number_set)






print("====== Specific operators =======")
# | & - ^
a = {10, 20, 50}
b = {20, 40}

result1 = a | b      # union -> Ikki setdagi hamma unique elementlarni birlashtiradi
result2 = a & b      # intersection -> Faqat ikkalasida ham bor elementlarni topadi
result3 = a - b      # difference -> A setda bor, lekin B da yo‘q elementlar
result4 = a ^ b      # symmetric difference -> ❌ ikkalasida ham bor narsani olib tashlaydi


print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)

