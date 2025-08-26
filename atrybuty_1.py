class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Objekt utworzony")

    def get_full_name(self):
        return f"{self.name} {self.age}"

    def __del__(self):
        print("Objekt usuniety " + self.get_full_name())


person = Person("Arek", 20)
print(person.get_full_name())
del person
