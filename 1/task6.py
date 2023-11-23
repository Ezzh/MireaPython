from collections import defaultdict

# Стандартные размеры материалов
standard_sizes = {
    'брус 50': 3,
    'брус 100': 6,
    'доска 25': 6,
    'доска 50': 6,
    'фанера': 1.5
}

def calculate_materials(order):
    # Создаем словарь для хранения количества необходимых материалов
    required_materials = defaultdict(float)

    # Обрабатываем каждую позицию в заказе
    for item, quantity, length in order:
        size = f'{item} {length}м'
        required_materials[size] += quantity

    # Сравниваем с общим объемом стандартных размеров материалов
    optimal_order = defaultdict(int)
    for size, quantity in required_materials.items():
        standard_size = size.rsplit(' ', 1)[0]
        if standard_size in standard_sizes:
            standard_length = standard_sizes[standard_size]
            optimal_quantity = (quantity * length) / standard_length
            optimal_order[standard_size] += optimal_quantity

    return optimal_order

# Пример использования
order = [
    ('брус 50', 3, 2),
    ('брус 50', 4, 1.5)
]

result = calculate_materials(order)

print("Оптимальный заказ:")
for size, quantity in result.items():
    print(f'{int(quantity)}x {size}')
