# Дана строка, содержащая полное имя файла.
# Выделить из этой строки название последнего каталога
# (без символов «/»).
# Если файл содержится в корневом каталоге, то вывести символ «\»
import os

file_path = input('Введите полное имя файла: ')
directory_name = os.path.basename(os.path.dirname(file_path))

if directory_name == "":
    directory_name = "\\"

print(directory_name)
