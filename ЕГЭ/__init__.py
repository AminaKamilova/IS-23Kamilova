
os.system("move pz_6/*.txt test")
os.system("move pz_7/*.txt test/test1")
os.rename("test/test1/*.txt", "test/test1/test.txt")

# 3. Выводим информацию о размере файлов в папке test
print("\nИнформация о размере файлов в папке test:")
for filename in os.listdir("test"):
    if os.path.isfile(os.path.join("test", filename)):
        size = os.path.getsize(os.path.join("test", filename))
        print(f"{filename}: {size} байт")

# 4. Переходим в pz_11 и находим файл с самым коротким именем
os.chdir("C:/Users/89615/OneDrive/Документы/оаип гит/pz_11")
shortest_filename = None
shortest_length = float('inf')

for filename in os.listdir():
    if os.path.isfile(filename):
        length = len(os.path.basename(filename))
        if length < shortest_length:
            shortest_length = length
            shortest_filename = filename

print("\nФайл с самым коротким именем в pz_11:", shortest_filename)

os.chdir("..")
os.chdir("папка_с_PDF_отчетом")
os.startfile("отчет.pdf")

# 6. Удаляем файл test.txt
os.remove("test/test1/test.txt")
