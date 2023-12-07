# Дан список А размера N. Найти количество его промежутков монотонности
# то есть участков на которых его элементы возрастают или убывают)
import random
def monotonic_intervals_count(a):
    if not a or len(a) < 2:
        return 0


a = []
monotonic_intervals = 0
direction = 0
# Обработка исключений
n = input("Введите значение N: ")
while int != type(n):
    try:
        n = int(n)
    except ValueError:
        n = input("Введите значение N: ")
k = input("Введите значение K: ")
while int != type(k):
    try:
        k = int(k)
    except ValueError:
        k = input("Введите значение K: ")

for i in range(n):
    a.append(random.randint(1, 5))
for i in range(1, ):
    if a[i] > a[i - 1]:
        if direction != 1:
            monotonic_intervals = monotonic_intervals + 1
            direction = 1
    elif a[i] < a[i - 1]:
        if direction != -1:
            monotonic_intervals = monotonic_intervals + 1
            direction = -1
result = monotonic_intervals_count(a)
# Если элементы равны, направление остается неизменным
# 0 - не определено, 1 - возрастание, -1 - убывание
print(a)
print(result)