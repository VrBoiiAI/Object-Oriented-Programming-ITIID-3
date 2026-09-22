### Create a class named Car with the following attributes: brand, model, and color.
# Add a method called show_info() that prints the full information of the car.
# Then, create two objects of the Car class with differenct values and call the method to
# display their information.

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Color: {self.color}')

car1 = Car("Chevrolet", "Spark", "Green")
car2 = Car("Cadillac", "CTS", "Black")

car1.show_info()
car2.show_info()