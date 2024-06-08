# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются с использованием модуля OS:
#
# •	перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге.
#     Имена вложенных подкаталогов выводить не нужно.
# •	перейти в корень проекта, создать папку с именем test. В ней создать еще одну
#     папку test1. В папку test переместить два файла из П36, а в папку test1 один файл из П37.
#     Файл из П37 переименовать в test.txt. Вывести в консоль информацию о размере файлов в папкe test.
# •	перейти в папку с PЗ11, найти там файл с самым коротким именем, имя вывести в консоль.
#     Использовать функцию basename() os.path.basename()).
# •	перейти в любую папку где есть отчет в формате pdf и «запустите» файл в привязанной к нему
#     программе. Использовать функцию os.startfile().
# •	удалить файл test.txt.

import os
os.chdir("C:/Users/89615/OneDrive/Документы/оаип гит/pz_11")
for dirpath, dirnames, filenames in os.walk("."):
     for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
     for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
# os.chdir("..")
# os.mkdir("test")
# os.mkdir("test/test1")
# os.replace("pz_6/file1(6).py", "test/file1(6).py")
# os.replace("pz_6/file2(6).py", "test/file2(6).py")
#
# os.replace("C:/Users/89615/OneDrive/Документы/оаип гит/pz_7/file1(7).py", "test/test1/file1(7).py")
# os.rename("test/test1/file1(7).py", "test/test1/test.txt")

print("Размер файлов в папкe test:")
for filename in os.listdir("C:/Users/89615/OneDrive/Документы/оаип гит/test"):
    if os.path.isfile(os.path.join("C:/Users/89615/OneDrive/Документы/оаип гит/test", filename)):
        size = os.path.getsize(os.path.join("C:/Users/89615/OneDrive/Документы/оаип гит/test", filename))
        print(f"{filename}: {size} байт")

os.chdir("C:/Users/89615/OneDrive/Документы/оаип гит/pz_11")
shortest = min(os.listdir(), key=len)
print("Файл с самым коротким именем в папке pz_11:")
print(os.path.basename(shortest))

os.chdir("..")
os.chdir("C:/Users/89615/OneDrive/Документы/оаип гит/reports")
os.startfile("ОТчёт по пз2..pdf")
# os.remove("C:/Users/89615/OneDrive/Документы/оаип гит/test/test1/test.txt")