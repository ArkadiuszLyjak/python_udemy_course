def remove_file_from_disc(file_path):
    import os
    os.remove(file_path)
    # spradz czy plik istnieje i napisz odpowiedni komunikat
    if os.path.exists(file_path):
        print("Plik został usunięty.")
    else:
        print("Plik nie istnieje.")
