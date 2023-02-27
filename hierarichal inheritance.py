# Define a base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Define a subclass of Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Define another subclass of Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Define a subclass of Cat
class Lion(Cat):
    def speak(self):
        return "Roar!"

# Create instances of each class and call their speak methods
animal = Animal("Generic animal")
print(animal.speak())  # Raises NotImplementedError

dog = Dog("Fido")
print(dog.speak())  # "Woof!"

cat = Cat("Whiskers")
print(cat.speak())  # "Meow!"

lion = Lion("Simba")
print(lion.speak())  # "Roar!"
