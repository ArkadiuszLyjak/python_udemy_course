import os

script_dir = os.path.dirname(__file__)
print(script_dir)

string_to_write = "zażółć wołowa"
# jesli plik ogonki.txt istnieje, to wpisz do niego "zażółć wołowa" a jesli nie, to utworz plik ogonki.txt i wpisz do niego "zażółć wołowa"
file_path_1 = os.path.join(script_dir, "ogonki.txt")
print(file_path_1)

if not os.path.exists(file_path_1):
    with open(file_path_1, "w", encoding="utf-8") as file:
        file.write(string_to_write)
else:
    with open(file_path_1, "a", encoding="utf-8") as file:
        file.write(string_to_write)
