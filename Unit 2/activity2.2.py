# Create a class Accountant with a method generate_report() that prints
# "Generating financial report".
# Create a class Technician with a method  repair_machine() that prints "Repairing machine".
# Create a class Boss that inherits from both classes and test both methods.

class Accountant:
    @staticmethod
    def generate_report():
        print("Generating financial report.")

class Technician:
    @staticmethod
    def repair_machine():
        print("Repairing machine.")

class Boss(Accountant, Technician):
    pass

acc1 = Accountant()
acc1.generate_report()

tech1 = Technician()
tech1.repair_machine()

boss1 = Boss()
boss1.generate_report()
boss1.repair_machine()
        