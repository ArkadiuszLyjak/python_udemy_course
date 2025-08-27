class Vehicle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.__max_speed = 199

    def __get_max_speed_info(self):
        return self.__max_speed

    def print_vehicle_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Max speed: {self.__get_max_speed_info()}")

vehicle = Vehicle("Audi", "A4", "czarny")
vehicle.print_vehicle_info()
# print(vehicle.__max_speed)
print(vehicle._Vehicle__max_speed)
print(vehicle.__get_max_speed_info())