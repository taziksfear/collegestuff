with open('text18-27.txt') as f:
    content = f.read()
    space_count = content.count(' ')
    lines = content.split('\n')

user_input = input("Введите фразу для последней строки: ")
lines[-1] = user_input

with open('poem_output.txt', 'w') as f:
    f.write('\n'.join(lines))

print(f"Количество пробельных символов: {space_count}")