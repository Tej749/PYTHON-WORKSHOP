class Bank:
    def __init__(self, balance, ac_number):
        self.__balance = balance
        self.ac_number = ac_number





    def deposit(self, deposit_amnt):
        self.deposit_amnt = deposit_amnt
        print(f"Amount Rs.{deposit_amnt}/- successfully deposited.....!!")
        self.__balance = self.__balance + deposit_amnt
        print(f"Your total bal is Rs.{self.__balance}/-....!!")
        print(self.ac_number)
        print(self.baz)



rohit = Bank(50000, 12345678)
rohit.deposit(3000)

