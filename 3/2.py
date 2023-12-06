ln = input("Введите строки. Когда закончите напишите 'стоп': ")
with open("bebebe.txt", "w") as f:
    while ln != "стоп":
        f.write(ln + "\n")
        ln = input()
