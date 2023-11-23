dictionary = input("Введите проверочные слова через пробел: ").split()
slova = input("Введите слова которые нужно проверить: ").split()


def find_same_word(word: str, wordlist: list):
    same_letters = 0
    dictionary = {}
    for i in range(len(wordlist)):
        for letter in range(min(len(wordlist[i]), len(word))):
            if wordlist[i][letter] == word[letter]:
                same_letters += 1
        dictionary.update([(same_letters, i)])
        same_letters = 0
    return wordlist[dictionary[max(dictionary)]]

result = ""
for word in slova:
    right_word = find_same_word(word, dictionary)
    if len(word) != len(right_word):
        result += word
    elif word == right_word:
        continue
    else:
        for letter in range(len(word)):
            if word[letter] != right_word[letter]:
                result += f" {word[letter]} "
            else:
                result += word[letter]
    result += " "

print(result)
