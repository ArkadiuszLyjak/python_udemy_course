class Employee:
    'Klasa przechowujaca informacje o pracownikach'
    numbers_of_employees = 0
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.numbers_of_employees += 1
        Employee.employees.append(self)
        print(Employee.__name__)
        print(Employee.__module__)
        setattr(self, 'age', 20)

    @staticmethod
    def print_doc_string():
        print(Employee.__doc__)

    @staticmethod
    def print_number_of_employees():
        print(Employee.numbers_of_employees)


employee1 = Employee("Arek", 1000)
employee2 = Employee("Ewa", 2000)
employee3 = Employee("Kasia", 3000)

# print(Employee.numbers_of_employees)
print(hasattr(employee1, 'name'))
print(hasattr(employee1, 'salary'))
print(getattr(employee1, 'age'))

for employee in Employee.employees:
    print(employee.name)

Employee.print_doc_string()
Employee.print_number_of_employees()
