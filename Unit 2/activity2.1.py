# Create a class Employee with attributes name and salary, and a method show_info()
# that prints the name and salary.
# Then, create a class Manager that inherits from Employee and adds an attribute department.
# Override show_info() to also display the department.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f'Name: {self.name}, Salary: {self.salary}')

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        print(f'Name: {self.name}, Salary: {self.salary}, Department: {self.department}')

employee1 = Employee("Arturo", 100)
manager1 = Manager("Javier", 250, "Accounting")
employee1.show_info()
manager1.show_info()