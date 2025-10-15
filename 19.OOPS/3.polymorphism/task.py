class Bird:
    def speak(self):
        print("Chirp")

class Dog:
    def speak(self):
        print("Bark")

# Same function name ‘speak’, different behavior
for animal in (Bird(), Dog()):
    animal.speak()


# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class 1
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Using polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()
