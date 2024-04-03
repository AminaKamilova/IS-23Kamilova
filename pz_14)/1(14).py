# В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами
# (например, А. Ф. Куманиной и т.п.)
import re
with open('Dostoevsky.txt', 'r', encoding="utf-8") as file:
        file_1 = file.read()
        initials_pattern = r'\b[А-ЯЁ]\.\s[А-ЯЁ]\.\s[А-ЯЁ][а-яё]+\b'
        initials = re.findall(initials_pattern, file_1)
        print("Фамилии с инициалами в тексте:")
for i in initials:
    print(i)