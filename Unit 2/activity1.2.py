### Create a class name Person with a constructor that receives the parameters name, age,
# and city.
# Add a method called greet() that displays a message such as:
# "Hi, my name is Ana, I am 25 years old, and I live in Mexico."
# Create three objects of the Person class and make each one call the greet() method.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def greet(self):
        print(f'Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.')

person1 = Person("Alexa", 21, "Juarez")
person2 = Person("Donovan", 19, "Tepic")
person3 = Person("Arturo", 22, "Tepic")

person1.greet()
person2.greet()
person3.greet()