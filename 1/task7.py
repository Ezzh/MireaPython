import random
from collections import Counter

industries = [
    'Сельское хозяйство',
    'Легкая промышленность',
    'Тяжелая промышленность группы А',
    'Тяжелая промышленность группы Б',
    'Военно промышленный комплекс',
    'Наука',
    'Химическая промышленность'
]

num_republics = 5
republics = [f'Republic-{i}' for i in range(1, num_republics + 1)]

data = [(random.choice(republics), random.choice(industries)) for _ in range(50)]

developed = ['Тяжелая промышленность группы А', 'Военно промышленный комплекс']
balanced = ['Легкая промышленность', 'Наука']
underdeveloped = ['Сельское хозяйство', 'Тяжелая промышленность группы Б', 'Химическая промышленность']

industry_counter = Counter(data)
republic_stats = {republic: {'developed': 0, 'underdeveloped': 0} for republic in republics}

for (republic, industry), count in industry_counter.items():
    if industry in developed:
        republic_stats[republic]['developed'] += count
    elif industry in underdeveloped:
        republic_stats[republic]['underdeveloped'] += count

print("Статистика развития отраслей:")
print("=" * 30)

# 1. Самая отстающая отрасль
underdeveloped_stat = [(industry, count) for (_, industry), count in industry_counter.items() if industry in underdeveloped]
most_underdeveloped = max(underdeveloped_stat, key=lambda x: x[1])
print(f"1. Самая отстающая отрасль: {most_underdeveloped[0]}, отстающая на {most_underdeveloped[1]}")

# 2. Самая развитая отрасль
developed_stat = [(industry, count) for (_, industry), count in industry_counter.items() if industry in developed]
most_developed = max(developed_stat, key=lambda x: x[1])
print(f"2. Самая развитая отрасль: {most_developed[0]}, развитая на {most_developed[1]}")

# 3. Самая сбалансированная отрасль
balanced_stat = [(industry, count) for (_, industry), count in industry_counter.items() if industry in balanced]
most_balanced = max(balanced_stat, key=lambda x: x[1])
print(f"3. Самая сбалансированная отрасль: {most_balanced[0]}, сбалансированная на {most_balanced[1]}")

# 4. Статистика развития по каждой из республик
print("\nСтатистика развития по каждой из республик:")
for republic, stats in republic_stats.items():
    print(f"{republic}: Развито - {stats['developed']}, Неразвито - {stats['underdeveloped']}")
