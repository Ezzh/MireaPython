def f(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

print(f(1233))