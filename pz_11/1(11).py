# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать новый
# текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:

# Исходные данные:
# Количество элементов:
# Элементы в обратном порядке:
# Сумма элементов последней половины:
sequence = [3, -5, 8, -2, 1, 0, -4, 6]
num_elements = len(sequence)

reverse_sequence = sequence[::-1]
index = num_elements // 2
sum_last_half = sum(sequence[index:])
with open("new_file.txt", "w", encoding="utf-16") as file:
    file.write("Исходные данные: " + str(sequence) + "\n")
    file.write("Количество элементов: " + str(num_elements) + "\n")
    file.write("Элементы в обратном порядке: " + str(reverse_sequence) + "\n")
    file.write("Сумма элементов последней половины: " + str(sum_last_half) + "\n")
file.close()
print("Файл создан.")
