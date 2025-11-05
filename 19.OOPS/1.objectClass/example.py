# class
class animal: 
    # Constructor
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def sound(self):
        print("I make my Sound")



# Objects
dog = animal("tom","male")
cat = animal("cherry","female")
# cat.name = "Tommy"


print(dog.name)
print(cat.name)
cat.sound()

