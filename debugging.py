''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''

import turtle

print("===== Python Packages & Core Package =====")
''' Python Packages/Modules: Core, File and External '''
# Core Packages > https://docs.python.org/3/library


# Core package
t = turtle.Turtle()

t.shape("turtle")
t.speed(2)
t.circle(150)
turtle.done()


my_file = open("material/message.txt", "r")    # opening the file in read mode "r"

try:
    content = my_file.read()       # Reads all text inside the file.
    print("content:", content)
finally:
    my_file.close()                # Closes the file no matter what happens (even if error comes)


# with
with open("material/message.txt", "r") as your_file:    # Python automatically closes file after block finishes ✅
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")


# Har bir core package — python package. Lekin har bir python package core package emas.








print("===== Package Manager & External Package =====")
''' Package Manager 
    Python > pip pipenv
    NodeJS > npm yarn
    PHP    > composer
    MacOS  > brew
'''
# External Package -> https://pypi.org/

 
from PIL import Image

with Image.open("material/logo.jpg") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")





print("===== Debugging =====")
def get_summary(*args):   # DEFINE args = (1, 2, 3, 4, 5)
    total_amount = 0

    for a in args:
        total_amount += a
        return total_amount   # find the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)   # CALL
print("result:", result)


