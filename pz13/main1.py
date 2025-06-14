numbers = list(map(int, input("Введите числа через пробел: ").split()))
filtered = [num for num in numbers if num > 0 and num % 3 == 0]
average = sum(filtered) / len(filtered) if filtered else 0
print(average)