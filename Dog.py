
class Dog:

    def __init__(self, p="WOOF"):
        self.phrase = p

    def bark(self):
        print(self.phrase)

    def changeBark(self, p):
        self.phrase = p


dog = Dog()
dog.bark()
dog.changeBark("meow")
dog.bark()
print("")
otherDog = Dog("HOOT")
otherDog.bark()
