class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Boww!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# create instances of the classes
dog = Dog()
cat = Cat()

# call the make_sound method on each instance
dog.make_sound() # outputs: "Boww!"
cat.make_sound() # outputs: "Meow!"
