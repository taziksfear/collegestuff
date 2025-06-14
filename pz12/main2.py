def uppercase_generator(s):
    for char in s:
        yield char.upper()

s = input("Введите строку: ")
print(''.join(uppercase_generator(s)))