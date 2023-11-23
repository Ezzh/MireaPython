import random

products_list = ['рыба', 'мясо', 'сталь', 'игрушки', 'книги', 'одежда', 'компьютеры', 'фрукты', 'автомобили', 'мебель', 'спорттовары', 'косметика', 'медикаменты', 'электроника', 'инструменты']

set1 = set(random.sample(products_list, random.randint(5, 10)))
set2 = set(random.sample(products_list, random.randint(5, 10)))


def find_uniq(set1, set2):
    return set1 ^ set2


print("\nНеповторяющиеся товары на обоих заводах:",*find_uniq(set1, set2))
