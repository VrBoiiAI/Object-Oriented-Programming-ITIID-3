# Create a function calculate_payment(worker) that calls a method payment() of the passed
# object. Create several classes (FullTimeEmployee, HourlyEmployee) each with its own 
# payment() method. Test the function with different objects and see how the same method
# produces different results.

class FullTimeEmployee:
    def payment(self):
        print("Full time employee payroll: $1000/day")

class HourlyEmployee:
    def payment(self):
        print("Hourly employee payroll: $100/hour")

def calculate_payment(worker):
    worker.payment()

ftemployee = FullTimeEmployee()
hemployee = HourlyEmployee()

calculate_payment(ftemployee)
calculate_payment(hemployee)