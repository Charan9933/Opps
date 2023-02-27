class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Bulldog(Dog):
    def __init__(self, name):
        super().__init__(name)
        
    def run(self):
        print(f"{self.name} is running")
        
bulldog = Bulldog("Spike")
bulldog.eat()  # output: Spike is eating
bulldog.bark()  # output: Spike is barking
bulldog.run()   # output: Spike is running
