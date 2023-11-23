def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файла нет")

read_and_print_file("bebebe")
