class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model} with {self.num_doors} doors"


my_car = Car("Toyota", "Corolla", 2022, 4)
print(my_car.get_info())  # 2022 Toyota Corolla with 4 doors
