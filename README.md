# Object-Oriented-Programming-ITIID-3

## Unit 1: Modeling
- Class Definition: Definition of an instance of a class Cellphone, its initialized values and methods.
- UML Use Case Diagram: Use case diagram detailing the interaction of a customer buying an appliance with store credit.
- UML Olympic Soccer Class Diagram: Class diagram explaining the parts and relationships of the classes within a soccer match.
- UML Car Reservation Class Diagram: Class diagram for the process of making a car rental.
- UML Sequence Diagram: Sequence diagram explaining the steps of making a reservation for a sport facility in a club.
---


## Unit 2: Syntax and documentation of object oriented languages
### Activity 1
- `activity1.1.py`: Create a class named Car with the following attributes: brand, model, and color. Add a method called show_info() that prints the full information of the car. Then, create two objects of the Car class with different values and call the method to display their information.
- `activity1.2.py`: Create a class name Person with a constructor that receives the parameters name, age, and city. Add a method called `greet()` that displays a message such as: "Hi, my name is Ana, I am 25 years old, and I live in Mexico." Create three objects of the Person class and make each one call the `greet()` method.
- `activity1.3.py`: Create a class named BankAccount with the following characteristics:
  - A class attribute named bank = "Central Bank"
  - An instance method named show_balance() that prints the client's balance.
  - A class method naed show_bank() that prints the bank's name.
  - A static method named convert currency(value) that receives an amount in dollars and converts it to pesos (use a fixed exchange rate of your choice).  
<br>
### Activity 2
- `activity2.1.py`: Create a class Employee with attributes name and salary, and a method `show_info()` that prints the name and salary. Then, create a class Manager that inherits from Employee and adds an attribute department. Override `show_info()` to also display the department.
- `activity2.2.py`: Create a class Accountant with a method `generate_report()` that prints "Generating financial report". Create a class Technician with a method `repair_machine()` that prints "Repairing machine". Create a class Boss that inherits from both classes and test both methods.
- `activity2.3.py`: Create a function `calculate_payment(worker)` that calls a method `payment()` of the passed object. Create several classes (FullTimeEmployee, HourlyEmployee) each with its own `payment()` method. Test the function with different objects and see how the same method produces different results.
- `activity2.4.py`: Create a class Engine with a method `start_engine()` that prints "Engine started". Create a class Car that has an attribute engine (type Engine) and a method `start_car()` that calls `engine.start()`.
- `activity2.5.py`: Create a class Book with attributes title and num_pages. Override:
  - `__str__()` to print "Book: X, Pages: Y".
  - `__len__()` so that len(book) returns the number of pages.