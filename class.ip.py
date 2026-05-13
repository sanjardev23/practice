'''CLASS deep diving
(1) ENCAPSULATION
(2) INHERITANCE
(3) POLIMORPHISM
'''




print("==== INHERITANCE ====")
# PARENT > CHILD (method va state`larni meros qilib olish)
# PARENT only provides public and protected proporties( state + method) to CHILD, but not private ones

class Animal:  # PARENT class
    # state
    description = "This class PARENT for animals"

    # constructor
    def __init__(self, voice):
        self._status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


# CHILD classes > Dog, Cat, Fish
class Dog(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # parent classining constructorini chaqirish uchun super() methodidan foydalanamiz
        super().__init__(voice)

    # method
    def indroduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")


class Cat(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # parent classining constructorini chaqirish uchun super() methodidan foydalanamiz
        super().__init__(voice)

    # method
    def indroduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        print("Yes, I can play with you!")


class Fish(Animal):
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        # parent classining constructorini chaqirish uchun super() methodidan foydalanamiz
        super().__init__(voice)

    # method
    def indroduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim!")


dog = Dog("Rex", "Woof", True)
cat = Cat("Tom", "Meow", True)
fish = Fish("Nemo", "zzzz", False)


dog.indroduce()
cat.indroduce()
fish.indroduce()


print("------")
dog.make_voice()
fish.make_voice()


print("------")
print(Animal.description)
print(Dog.description)


print(dog.voice, fish.voice)
print("dog status:", dog._status)
print("cat status:", cat._status)
print("fish status:", fish._status)
