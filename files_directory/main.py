import os

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, "test.txt")
    # print(path)
    file_handle = open(path, "w", encoding="utf-8")
    file_handle.write("Hello World")
    file_handle.close()

    if os.path.exists(path):
        if os.path.isfile(path):
            print("Plik istnieje")
        else:
            print("To nie jest plik")
    else:
        print("Plik nie istnieje")

    # my_int = 8937
    # my_string = "Some string"
    # my_float = 3.14
    # my_list_names = ["Ewa", "Kasia", "Arek", "Ewa", "Kasia", "Arek"]
    #
    # data = (my_int, my_string, my_float, my_list_names)
    #
    # NBYTES = 4096  # ile bajtów zapisać
    # OUT_PATH = r"C:\repo\python_projects\udemy_courses\files_directory\data.pkl"
    # IN_PATH = r"C:\repo\python_projects\udemy_courses\files_directory\data.pkl"
    #
    # p = file_operations_pack.write_binary_to_file.save_tuple_pickle(OUT_PATH, data)
    # print("Zapisano do:", p.resolve())
    # print("Rozmiar pliku:", p.stat().st_size, "B")
    #
    # try:
    #     data = file_operations_pack.write_binary_to_file.load_tuple_pickle(IN_PATH)
    #     my_int, my_string, my_float, my_list_names = data
    #     print("int:", my_int)
    #     print("string:", my_string)
    #     print("float:", my_float)
    #     print("list:", my_list_names)
    #
    # except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
    #     print(e)
