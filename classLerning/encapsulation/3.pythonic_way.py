class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def pay(self):          # property name = "pay"
        return self.__salary

    @pay.setter
    def pay(self, value):   # attach setter to "pay"
        self.__salary = value


e = Employee(50000)
print(e.pay)     # getter
e.pay = 600    # setter
print(e.pay)
