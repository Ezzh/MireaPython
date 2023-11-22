from math import e, sin, cos

print("""Простейший калькулятор\n1. +\n2. -\n3. ÷\n4. x\n5. e**x+y\n6. sin(x+y)\n7. cos(x+y)\n8. x**y""")
choice = input()
x = int(input())
y = int(input())
print()
print("Ответ: ", end='')
if choice == "1":
    print(x + y)
elif choice == "2":
    print(x - y)
elif choice == "3":
    try:
        print(x / y)
    except Exception:
        print("Ошибка!")
elif choice == "4":
    print(x * y)
elif choice == "5":
    print(e**(x + y))
elif choice == "6":
    print(math.degrees(sin(x + y)))
elif choice == "7":
    print(math.degrees(cos(x + y)))
elif choice == "8":
    print(x ** y)