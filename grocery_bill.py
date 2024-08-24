class Item:
    def __init__(self, id, itemName, price):
        self.id = id
        self.itemName = itemName
        self.price = price


# create bill display function

def display(self, cName, cAddress):
    total = 0
    print("\n\n\n")
    print("\t    Kellme Store   ")
    print("\t    -------------   ")
    print(f'Name : {cName} \t Address : {cAddress}\n')

    for obj in 1:
        print(f"ID : {obj.id}\t itemName : {obj.itemName} \t Price : {obj.price}")
        print("------------------------------------------------------------------")
        total += obj.price
    print(f'\t\tTotal : {total}')
    print("\n")
    print("\t Thanks for Visiting")
    print("\n\n")


# store object array
list = []

print("\n\n")
print("Hello Everyone")
cName = input("Enter your Name : ")
cAddress = input("Enter your Address : ")
totalItems = int(input("Enter Total Items : "))
print("\n")

# take input item details

for i in range(0, totalItems):
    id = (i + 1)
    name = input("Enter item name : ")
    price = int(input("Enter Price : "))
    list.append(Item(id, name, price))

# call display function

display(list, cName, cAddress)
