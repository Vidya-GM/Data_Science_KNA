# This is Solution-2 of Assignment payment System, where focus is "abstraction + polymorphism2
from abc import ABC, abstractmethod
import time

'''
This impliemntation of PaymentSystem has following classes:
    1. AddMoney(ABC)
    2. CreditCard(AddMoney)
    3. UPI(AddMoney)

    4. PaymentSystem

- AddMoney is an abstract class, which has abstractmethod "add_cash" 
    which is why it's child classes 'CreditCard', and 'UPI' need to implement 'add_cash' method

- PaymentSystem class has init method which initialises 1000(as initial balance)
    It has following methods:
        1. add_money_to_system
            This method has a variable 'method: AddMoney' which shows that it is an object of AddMoney class
            As AddMoney(ABC) has two child classes, so this method  object can be of either CreditCard or UPI class
        2. refund
        3. show_transaction_history --> This method shows history (protected attribute of PaymentSystem)
        4. show_system_balance

For execution, we need to create an object of PaymentSystem, then when we use 'add_money_to_system' method
This method need an attribute 'method' which is an object of CreditCard, UPI.
So need to create an object of CreditCard, UPI, and depending on user choice this will attribute of 
add_money_to_system

'''


class AddMoney(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_cash(self):
        pass


class CreditCard(AddMoney):
    def add_cash(self, money):
        print(f"{money} added to system account using Creditcard")


class UPI(AddMoney):
    def add_cash(self, money):
        print(f"{money} added to system account using UPI")


class PaymentSystem:
    def __init__(self):
        self.store_account_balance = 1000

        self.__transaction_history = []

    def add_cash_to_system(self, money, method: AddMoney):
        method.add_cash(money)
        self.store_account_balance += money
        c_t = time.ctime()

        self.__transaction_history.append({f"At_{c_t}": f"{money} Added to SystemAccount"})

    def refund_money(self, money):
        if self.store_account_balance > money:
            self.store_account_balance -= money
        print(f"{money} refunded from system account ")

        c_t = time.ctime()
        self.__transaction_history.append({f"At_{c_t}": f"{money} refunded from SystemAccount"})

    def show_transaction_history(self):
        for i in self.__transaction_history:
            print(i)

    def show_system_acc_balance(self):
        print(f"System Account Balance is: {self.store_account_balance}")


# s1 = PaymentSystem()
# a1 = CreditCard()

# s1.add_cash_to_system(method=a1, money=200)
# s1.add_cash_to_system(method=a1, money=300)
# s1.show_transaction_history()
# s1.show_system_balance()