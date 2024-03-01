# This is a code that describes cars
#CLASS
class car:
    def __init__(self, make, model, horsepower, fuelcapacity, colour):
        self.make = make
        self.model = model
        self.horsepower = horsepower
        self.fuelcapacity = fuelcapacity
        self.colour = colour

def print_make(self,make):
    print("The car is of {0}make" . format(self.make))

def set_make(self,make):
    self.make = make

def get_make(self):
    return self.make

car.set_make("dodgechallenger") 
print(car.get_make())

mycar= car ("volkswagen", "Golf", "147HP", "20l", "metallic blue")

