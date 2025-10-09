class Bird:
    def speak(self):
        print("Chirp")

class Dog:
    def speak(self):
        print("Bark")

# Same function name ‘speak’, different behavior
for animal in (Bird(), Dog()):
    animal.speak()
