import time

t = input("Введите количество часов, минут и секунд через пробел: ").split()
seconds = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[0])
while seconds:
    print(f"Осталось {seconds // 3600} часов {seconds % 3600 // 60} минут {seconds % 3600 % 60} секунд" )
    time.sleep(1)
    seconds -= 1