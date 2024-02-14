# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать новый
# текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

# Исходные данные:
# Количество элементов:
# Элементы в обратном порядке:
# Сумма элементов последней половины:
with open('number_sequence.txt', 'w') as sequence_file:
    sequence = [3, -5, 8, -2, 1, 0, -4, 6]
    for num in sequence:
        sequence_file.write(str(num) + ' ')

# Чтение последовательности из файла и выполнение обработки
with open('number_sequence.txt', 'r') as sequence_file:
    numbers_from_file = [int(num) for num in sequence_file.read().split()]

num_elements = len(numbers_from_file)
reverse_sequence = numbers_from_file[::-1]
index = num_elements // 2
sum_last_half = sum(numbers_from_file[index:])

with open("new_file.txt", "w", encoding="utf-16") as file:
    file.write("Исходные данные:" + str(numbers_from_file) + "\n")
    file.write("Количество элементов: " + str(num_elements) + "\n")
    file.write("Элементы в обратном порядке: " + str(reverse_sequence) + "\n")
    file.write("Сумма элементов последней половины: " + str(sum_last_half) + "\n")

print("Файлы созданы.")
