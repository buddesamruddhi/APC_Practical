class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

print("Enter details for Account 1")
name1 = input("Enter account holder name: ")
account_number1 = input("Enter account number: ")
balance1 = float(input("Enter balance: "))

account1 = BankAccount(name1, account_number1, balance1)

print("\nEnter details for Account 2")
name2 = input("Enter account holder name: ")
account_number2 = input("Enter account number: ")
balance2 = float(input("Enter balance: "))

account2 = BankAccount(name2, account_number2, balance2)


print("\n--- Account Details ---")
account1.display()
account2.display()