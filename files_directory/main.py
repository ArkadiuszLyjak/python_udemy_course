import os

import file_operations_pack

string_to_write = "zażółć wołowa"

file_path_1 = "C:\\repo\\python_projects\\udemy_courses\\files_directory\\test_00.txt"
folder = os.path.dirname(file_path_1)
print(folder)

file_name = os.path.basename(file_path_1)
print(file_name)

name, extension = os.path.splitext(file_name)
print(name)
print(extension)

drive, _ = os.path.splitdrive(file_path_1)
print(drive)

file_operations_pack.write_string_to_file(folder, string_to_write)
# file_operations_pack.read_from_file(file_path_1)
# file_operations_pack.rename_file(file_path_1, "test_01.txt")
# file_operations_pack.remove_file_from_disc(file_path_1)
