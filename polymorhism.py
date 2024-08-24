class Many:
    def bigyan(self):
        print("hello")

    def bigyan(self, teacher=''):
        print("hello", teacher)

    def bigyan(self, teacher='', student=''):
        print("hello", teacher, student)

obj = Many()
obj.bigyan()
obj.bigyan(teacher='bigyan')
obj.bigyan(teacher='bigyan', student="Najuma")

print(10 + 10)
print("10" + "10")
print(10 * 10)
