# a class that inherit all method & properties from one class to another class is called inheritance.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f'{self.brand} is start an engine....!!')


class Car(Vehicle):
    def __init__(self, brand, color, speed):
        super().__init__(brand)
        self.color = color
        self.speed = speed

    def drive(self):
        print(f'{self.brand} & {self.color} is driving with speed {self.speed}')


fiat = Car("FIAT-100S", 'Black', '320 KM/Hr')
fiat.drive()
fiat.start_engine()

