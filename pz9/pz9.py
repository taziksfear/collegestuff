words = {
    'apple': 'яблоко',
    'house': 'дом',
    'cat': 'кот',
    'dog': 'собака',
    'book': 'книга',
    'water': 'вода',
    'sun': 'солнце',
    'tree': 'дерево',
    'car': 'машина',
    'city': 'город'
}

rus_words = {v: k for k, v in words.items()}

word = input('Введите слово: ').lower()
print(words.get(word, rus_words.get(word, 'Нет в словаре')))
