class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("Toyota", "Corolla", 2022)

print("Car Details:")
print(f"Brand: {car1.brand}")
print(f"Model: {car1.model}")
print(f"Year: {car1.year}")
