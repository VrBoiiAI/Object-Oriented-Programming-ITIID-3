# Create a class Engine with a method start_engine() that prints "Engine started".
# Create a class Car that has an attribute engine (type Engine) and a method start_car()
# that calls engine.start().

class Engine:
    def start_engine(self):
        print("Engine started")

class Car:
    engine = Engine()
    def start_car(self):
        self.engine.start_engine()

car1 = Car()
car1.start_car()