class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years oldaaaaaa"


user_1 = User("John", 30)


# print(user)


class Employee(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f"{self.name} is {self.age} years old and earns {self.salary}"


employee_1 = Employee("Alice", 25, 50000)
# print(employee)
