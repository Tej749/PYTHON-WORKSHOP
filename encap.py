# Encapuslation : wrapping the data in single unit

class BankClass:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number


    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f"deposited {deposit_amount}")
        print(f'Balance Amount {self.balance}')
        # print(self.balance)
        # print(self.account_number)


prashna = BankClass(25000, 12345)
prashna.deposit(5000)



