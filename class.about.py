'''CLASS
    (1) What is class
    (2) Ordinary vs static properties
    (3) Special methods
'''
print("==== What is class ====")
# class - blueprint for object creation!
# structure > state


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Justin", 25)
person2 = Person("Simon", 23)
person3 = Person("John", 30)

# ordinary state property
print("Person1.name:", person1.name)


# ordinary method
person1.introduce()
person2.say_age()


print("==== Ordinary vs static properties ====")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
