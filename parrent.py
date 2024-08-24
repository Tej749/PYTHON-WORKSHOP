class Vehicle:  # parant class, super class
    def __init__(self, brand):  # instance constructor, properties
        self.brand = brand  # instance attribute

    def start_engine(self):
        print(f'{self.brand} is starting an engine...!')        # parent class : instance method


class Car(Vehicle):  # child/derive class
    def __init__(self, brand, speed):
        super().__init__(brand)
        self.speed = speed

    def drive(self):
        print(f'{self.brand} is driving with speed {self.speed} an engine...!')


thar = Car("Thar 4 x 4", '2000 Km/Hr')
thar.drive()
thar.start_engine()

bmw = Car('BMW-100', '400 KM/HR')
bmw.drive()
bmw.start_engine()


