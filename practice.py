class animal:
    def sound(self):
        print("I am a Animal")
    

class dog(animal):
    def sound(self):
        print("I am a Dog")

class cat(animal):
    def sound(self):
        print("I am a cat")


ani = animal()
mycat = cat()
mydog = dog()

# ani.sound()
# mycat.sound()
# mydog.sound()

animals = [ani, mycat, mydog]

for a in animals:
    a.sound()
