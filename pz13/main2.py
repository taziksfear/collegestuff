n = int(input("Введите номер строки N: "))
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[n] = [x + 3 for x in matrix[n]]
print(matrix)