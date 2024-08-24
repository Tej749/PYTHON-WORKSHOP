class Vehicle:  # Parant Class
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} is starting an engine....!!")


class Car(Vehicle):  # Child Class
    def __init__(self, brand, model, speed):
        super().__init__(brand)
        self.model = model
        self.speed = speed

    def drive(self):
        print(f'{self.brand} & {self.model} is drive with speed {self.speed}...!')


bmw = Car("BMW-200S", 'B-2024', '320 KM/Hr')
bmw.drive()
bmw.start_engine()
