# import math

import random

from math_module import add_numbers

print(add_numbers(5, 6))
print(random.randint(1, 10000))


# funkcja ktora losuje 4 liczby z przedzialu od 1 do 10000 w petli, kazda nowa liczbe dodaje do popredniej,
# nastepnie wylicaa srednia i ja wyswietla
def random_numbers():
    numbers = []
    for i in range(4):
        numbers.append(random.randint(1, 10000))
    avg = sum(numbers) / len(numbers)
    print(avg)


random_numbers()
