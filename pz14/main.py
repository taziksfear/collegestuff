with open('Dostoevsky.txt') as f:
    content = f.read()

year = '1857 год'
start = content.find(year)
end = content.find('\n\n', start)

with open('Dostoevsky_1857.txt', 'w') as f:
    f.write(content[start:end])