def read_from_file(file_path):
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        lines = file.readlines()
        for line in lines:
            print(line)

        file.seek(0)
        print(file.readline())

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        print(file.tell())
