# Дан список А размера N. Найти количество его промежутков монотонности
# то есть участков на которых его элементы возрастают или убывают)
import random
def count_monotone_intervals(arr):
    increasing = decreasing = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            increasing += 1
        elif arr[i] < arr[i - 1]:
            decreasing += 1
    return increasing, decreasing
a = []
# Пример списка A
n = input("Введите значение N: ")
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input("Введите значение N: ")
for i in range(n):
    a.append(random.randint(1, 5))

# Вычисление количества участков возрастания и убывания
increasing_count, decreasing_count = count_monotone_intervals(a)
print("Список: ", a)
print("Количество участков возрастания: ", increasing_count)
print("Количество участков убывания: ", decreasing_count)
