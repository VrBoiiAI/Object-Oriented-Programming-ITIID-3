### Create a class named BankAccount with the following characteristics:
# - A class attribute named bank = "Central Bank"
# - An instance method named show_balance() that prints the client's balance.
# - A class method naed show_bank() that prints the bank's name.
# - A static method named convert currency(value) that receives an amount in dollars and
#   converts it to pesos (use a fixed exchange rate of your choice).

class BankAccount:
    bank = "Central Bank"

    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f'Balance: {self.balance}')

    @classmethod
    def show_bank(self):
        print(f'{self.bank}')

    @staticmethod
    def convert_currency(dollars):
        return dollars * 17.46 # as of sept 21st

bankAccount1 = BankAccount(1000)
bankAccount1.show_balance()
bankAccount1.show_bank()
print(BankAccount.convert_currency(6))