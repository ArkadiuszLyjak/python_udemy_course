class Vehicle:
    def __init__(self):
        self.brand = "unknown"
        self.model = "unknown"
        self.color = "unknown"
        self.max_speed = 0

    def print_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Max speed: {self.max_speed}")


vehicle = Vehicle()

vehicle.print_info()


class Car(Vehicle):
    def print_info(self):
        self.brand = "Audi"
        self.model = "A4"
        self.color = "czarny"
        self.max_speed = 200
        super().print_info()


car = Car()
car.print_info()
