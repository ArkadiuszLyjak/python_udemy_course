class Car:
    def __init__(self, make, model, /, year, *, color="bezbarwny", top_speed=0, price):
        if not isinstance(make, str):
            raise TypeError("make musi być typu string")
        if not isinstance(model, str):
            raise TypeError("model kaputy musi być typu string")

        if not isinstance(year, int):
            raise TypeError("rok produkcji musi być typu int")
        if not isinstance(color, str):
            raise TypeError("kolor musi być typu string")
        if not isinstance(price, float):
            raise TypeError("cena musi być typu float")

        if top_speed < 0 or top_speed is None:
            raise ValueError("top_speed musi być większe od zera")

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price


audi = Car("Audi", "A4", 2019, color="czarny", top_speed=200, price=10000.0)
print(audi.make)
