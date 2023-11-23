import random


noun = input("Введите существительные до слова stop:\n")
nouns = []
while noun != "stop":
    nouns.append(noun)
    noun = input()


verb = input("Введите глаголы до слова stop:\n")
verbs = []
while verb != "stop":
    verbs.append(verb)
    verb = input()

for i in int(input("Введите количество фраз")):
    result = []
    result = [random.choice(nouns), random.choice(nouns)]
    result.append(random.choice(verbs))
    random.shuffle(result)
    print(*result)

