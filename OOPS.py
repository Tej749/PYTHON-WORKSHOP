class Car:
    def __init__(self, model, color, speed):        # instance constructor & properties , inline comment
        self.model = model
        self.color = color
        self.speed = speed      # instance attribute

    def start_engine(self):             # actopm : instance method
        print(f'{self.model} & {self.color} is starting an engine....!!')

    def drive(self):                # actopm : instance method
        print(f'{self.model} & {self.color} is driving with speed {self.speed}')

ferrari = Car("F-2024 Version", "Blue-Red", "500 KM/Hr")
ferrari.start_engine()
ferrari.drive()

bmw = Car("BMW-100", "Black", '1000Kh/hr')
bmw.start_engine()
bmw.drive()
'''
this is a multiline comment
'''






