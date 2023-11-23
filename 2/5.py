import time, random

while True:
    time.sleep(1)
    try:
        _ = 10 / random.randint(0, 1)
    except ZeroDivisionError:
        print("Деление на 0")
        continue
    print("Все норм")
    
