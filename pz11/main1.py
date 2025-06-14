import random

def generate_numbers(filename):
    numbers = [random.randint(-10, 10) for _ in range(10)]
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, numbers)))

generate_numbers('file1.txt')
generate_numbers('file2.txt')

with open('file1.txt') as f1, open('file2.txt') as f2:
    nums1 = list(map(int, f1.read().split()))
    nums2 = list(map(int, f2.read().split()))

common_in_1 = set(nums1) & set(nums2)
common_in_2 = common_in_1
negative_count = sum(1 for num in nums1 + nums2 if num < 0)
positive_count = sum(1 for num in nums1 + nums2 if num > 0)

with open('result.txt', 'w') as f:
    f.write(f"Элементы первого и второго файлов:\n{nums1}\n{nums2}\n")
    f.write(f"Элементы первого файла, присутствующие во втором:\n{common_in_1}\n")
    f.write(f"Элементы второго файла, присутствующие в первом:\n{common_in_2}\n")
    f.write(f"Количество элементов: {len(nums1) + len(nums2)}\n")
    f.write(f"Количество отрицательных элементов: {negative_count}\n")
    f.write(f"Количество положительных элементов: {positive_count}\n")