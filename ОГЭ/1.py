# B файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения OT 1 до 100 000 включительно.
# Определите количество троек элементов последовательности, в которых только одно из чисел
# является четырёхзначным, а сумма элементов тройки не меньше максимального элемента
# последовательности, оканчивающегося на 15
# В ответе запишите количество найденных троек чисел,
# затем максимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих
# подряд элемента последовательности.

with open('ttt.txt') as sequence:
    numbers_from_file = [int(num) for num in sequence.readlines()]
max_ending_15 = max(numbers_from_file[i:i+3] for i in range(0, len(numbers_from_file), 3) if numbers_from_file[i] % 10 == 1 and numbers_from_file[i+1] % 10 == 5)
max_ending_15 = max(max_ending_15)
count = 0
max_sum = 0
for i in range(1, len(numbers_from_file)-1):
    if (numbers_from_file[i] > 999) ^ (numbers_from_file[i-1] > 999) ^ (numbers_from_file[i+1] > 999):
        sum3 = numbers_from_file[i-1] + numbers_from_file[i] + numbers_from_file[i+1]
        if sum3 >= max_ending_15:
            count += 1
            max_sum = max(max_sum, sum3)

print("Количество найденных троек чисел:", count, "\n" "Максимальная из сумм элементов таких троек:", max_sum)

