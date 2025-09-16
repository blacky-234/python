class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private

    # getter
    def get_balance(self):
        return self.__balance

    # setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

acc = BankAccount(1000)
print(acc.get_balance())   # 1000
acc.deposit(500)
print(acc.get_balance())   # 1500

acc.__balance = 2000  # AttributeError
print("modify not working : ",acc.get_balance())
