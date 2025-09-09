from functools import reduce

sum = lambda a, b: a + b


# print(sum(2, 3))


def genFunc(n):
    return lambda x: x ** n


# print(genFunc(3)(2))

list_of_names = ["Arek", "Ewa", "Kasia"]

result = filter(lambda x: len(x) < 4, list_of_names)
# print(list(result))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numSum = reduce((lambda x, y: x + y), numbers)


# print(numSum)


def generate_lambda(n):
    return lambda x: x * n


doubler = generate_lambda(2)
# print(doubler(5))

# print(list(map(generate_lambda(2), numbers)))

greater_than_5 = lambda x: x > 5
# print(list(filter(greater_than_5, (map(generate_lambda(2), numbers)))))


girl_names = ["Ewa", "Kasia", "Arek"]


def add_surname(surname):
    return lambda name: f"{name.capitalize()} {surname.capitalize()}"


print(list(map(add_surname("kowalska"), girl_names)))
