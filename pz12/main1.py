n = int(input("Введите нечётное N: "))
sequence = [int(input()) for _ in range(n)]
half = n // 2
product = 1

for num in sequence[:half]:
    if num < 0:
        product *= num

print(product)