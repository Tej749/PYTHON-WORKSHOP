class Car:
    def __init__(self, model, color, speed):    # Instance constructor, manufacturing phase, Object properties
        self.model = model      # instance attribute
        self.color = color
        self.speed = speed

    def start_engine(self):         # Action , instance method
        print(f'{self.model} & {self.color} is starting an engine.....!')

    def drive(self):
        print(f'{self.model} & {self.color} is drive with speed {self.speed}.....!')


bmw = Car("BMW-100", 'GREY', "320 KM/Hr")       # object call, output 
bmw.start_engine()
bmw.drive()

ford = Car("Ford-200", 'Black', "520 KM/Hr")
ford.start_engine()
ford.drive()