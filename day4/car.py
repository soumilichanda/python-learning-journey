class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : ${self.price}")


# Example usage:
my_car = Car("Toyota", "Camry", 25000)
my_car.display_details()