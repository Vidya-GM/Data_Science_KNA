from OOP_Assignment_Sol1 import StorePaymentSystem
import sys


s1 = StorePaymentSystem()
print("\nWelcome to Payment System!\n")
print("Your Options :" \
        "\nPress '1': Add Cash to the System " \
        "\nPress '2': Refund Money " \
        "\nPress '3': Check balance " \
        "\nPress '4': Check Transactions " \
        "\nPress '5' Exit the System")


while True:
    users_choice = input("Enter your option: ")

    if users_choice == '1':
        amount = int(input("Enter amount to be added: "))
        pay_option = input("Choose payment option: \nFor Credit-Card Press 'C'  \nFor UPI Press 'U':  ")
        if pay_option.lower() == 'c':
            method = "Credit-card"
        elif pay_option.lower() == 'u':
            method = "UPI"
        else:
            print("Invalid option!")
            break
        s1.add_cash_to_system(method, amount)
        cnt = input("press 'Y' to continue")
        if cnt.lower() != 'y':
            break
    elif users_choice == '2':
        amount = int(input("Enter amount to be added: "))
        s1.refund_money(amount)
        
    elif users_choice == '3':
        s1.show_store_acc_balance()
        
    elif users_choice == '4':
        s1.show_transaction_history()
    elif users_choice == '5':
        print("Exiting the PaymentSystem")
        sys.exit(0)
    else:
        print("Invalid Choice!")
        break
