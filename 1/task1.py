print("""Простейший калькулятор\n1. +\n2. -\n3. ÷\n4. x\n5. x%y\n6. x**(1/y)\n7. x**y""")
choice = input()
x = int(input("Введите x:"))
y = int(input("Введите y:"))
print()
if choice == "1":
    print(x + y)
elif choice == "2":
    print(x - y)
elif choice == "3":
    try:
        print(x / y)
    except Exception:
        print("Error")
elif choice == "4":
    print(x * y)
elif choice == "5":
    try:
        print(x % y)
    except Exception:
        print("Error")
elif choice == "6":
    try:
        print(x**(1/y))
    except Exception:
        print("Error")
elif choice == "7":
    print(x ** y)