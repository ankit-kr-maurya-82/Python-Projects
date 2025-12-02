# Basic class and object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Mahindra", "Thar")
print(my_car.brand)