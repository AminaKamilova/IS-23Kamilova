# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются с использованием модуля OS:
#
# •	перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге.
#     Имена вложенных подкаталогов выводить не нужно.
# •	перейти в корень проекта, создать папку с именем test. В ней создать еще одну
#     папку test1. В паmky test переместить два файла из П36, а в папку test1 один файл из П37.
#     Файл из П37 переименовать в test.txt. Вывести в консоль информацию о размере файлов в папкe test.
# •	перейти в папку с PЗ11, найти там файл с самым коротким именем, имя вывести в консоль.
#     Использовать функцию basename() os.path.basename()).
# •	перейти в любую папку где есть отчет в формате pdf и «запустите» файл в привязанной к нему
#     программе. Использовать функцию os.startfile().
# •	удалить файл test.txt.

import os

# 1. Переход в каталог PZ11 и вывод списка файлов
os.chdir("PZ11")
print("Файлы в PZ11:")
for filename in os.listdir():
    if os.path.isfile(filename):
        print(filename)

# 2. Переход в корень проекта, создание папок test, test1 и перемещение файлов
os.chdir("..")  # Переход в корневой каталог
os.makedirs("test/test1", exist_ok=True)  # Создание папок, если они не существуют

# Перемещение двух файлов из PZ11/P36 в test
for i in range(2):
    filename = f"PZ11/P36/file{i+1}.txt"  # Предположим, что в P36 файлы называются file1.txt, file2.txt
    if os.path.exists(filename):
        os.rename(filename, f"test/file{i+1}.txt")

# Перемещение файла из PZ11/P37 в test1 и переименование
filename = "PZ11/P37/file.txt"  # Предположим, что в P37 файл называется file.txt
if os.path.exists(filename):
    os.rename(filename, "test/test1/test.txt")

# Вывод информации о размере файлов в папке test
print("\nРазмер файлов в папке test:")
for filename in os.listdir("test"):
    if os.path.isfile(os.path.join("test", filename)):
        size = os.path.getsize(os.path.join("test", filename))
        print(f"{filename}: {size} байт")

# 3. Переход в PZ11 и поиск файла с самым коротким именем
os.chdir("PZ11")
shortest_filename = min(os.listdir(), key=len)
print("\nФайл с самым коротким именем в PZ11:", shortest_filename)

# 4. Переход в папку с PDF и запуск в привязанной программе
os.chdir("..")  # Переход на уровень выше
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pdf"):
            pdf_path = os.path.join(root, file)
            os.startfile(pdf_path)
            break  # Запускаем только один PDF-файл
    if file.endswith(".pdf"):
        break  # Прерываем цикл, если нашли PDF

# 5. Удаление файла test.txt
os.remove("test/test1/test.txt")
