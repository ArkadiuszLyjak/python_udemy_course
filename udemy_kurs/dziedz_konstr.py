class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person konstruktor")

    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print()


class Student(Person):
    def __init__(self, name, age=0):
        Person.__init__(self, name, age)
        print("Student konstruktor")

    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print()


person = Person("Arek", 20)
person.print_info()

student = Student("Ewa", 65)
student.print_info()
