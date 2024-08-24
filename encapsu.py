class BankClass:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Deposit Rs.{amount}')
        print(f'Balance amount Rs.{self.__balance}')


pinto = BankClass(25000, 123456)
# pinto.deposit(2000)
print(pinto.balance)

