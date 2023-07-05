class Vehicle:
    def __init__(self, make, modle):
        self.make = make
        self.modle = modle

    def move(self):
        print("Moving along...")

    def get_make_modle(self):
        return f"I'm a{self.make} {self.modle}."


my_car = Vehicle("Toyota", "Corolla")
""" print(my_car.make)
print(my_car.modle) """
print(my_car.get_make_modle())
my_car.move()

Our_car = Vehicle("Cadillac", "Escalade")
print(Our_car.get_make_modle())
