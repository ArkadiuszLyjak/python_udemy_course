class Cars:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    @property
    def brand(self):
        return self._brand

    @property
    def color(self):
        if self._color == "czarny":
            raise ValueError("Czarny kolor jest niedopuszczalny")
        return self._color

    @brand.setter
    def brand(self, value):
        self._brand = value

    @color.setter
    def color(self, value):
        self._color = value


polonez = Cars("Polonez", "czarnyyyy")
print(polonez.brand)
print(polonez.color)

polonez.brand = "Audi"
polonez.color = "czerwony"
print(polonez.brand)
print(polonez.color)