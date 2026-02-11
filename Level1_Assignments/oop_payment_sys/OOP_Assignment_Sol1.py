# This is Solution-1 of oop assignment 'payment_system' where focus is 'abstractmethods'
from abc import ABC, abstractmethod
import time


class PaymentSystem(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_cash_to_system(self):
        pass

    @abstractmethod
    def refund_money(self):
        pass


class StorePaymentSystem(PaymentSystem):
    def __init__(self):
        self.store_account_balance = 1000

        self.__transaction_history = []

    def add_cash_to_system(self, method, amount):
        print(f"Added {amount} using {method}")
        self.store_account_balance += amount
        c_t = time.ctime()

        self.__transaction_history.append({f"At_{c_t}": f"{amount} Added to SystemAccount"})

    def refund_money(self, amount):
        if self.store_account_balance > amount:
            self.store_account_balance -= amount

        c_t = time.ctime()
        print(f"{amount} refunded from SystemAccount")
        self.__transaction_history.append({f"At_{c_t}": f"{amount} refunded from SystemAccount"})

    def show_transaction_history(self):
        for i in self.__transaction_history:
            print(i)

    def show_store_acc_balance(self):
        print(f"Store account balance is: {self.store_account_balance}")


# s1 = StorePaymentSystem()
# s1.add_cash_to_system(200)
# s1.show_transaction_history()
'''
class AddCash:
    def CreditCard(self):
        pass
        
    def UPI(self):
        pass
'''