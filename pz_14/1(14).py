# В исходном текстовом файле (Dostoevsky.txt) найти все фамилии с инициалами
# (например, А. Ф. Куманиной и т.п.)
import re
with open('Dostoevsky.txt', 'r', encoding="utf-8") as file:
        text = file.read()
        # Найдем фамилии с инициалами
        initials_pattern = r'\b[А-Я]\.\s[А-Я]\.\s[А-Я][а-я]+\b'
        initials = re.findall(initials_pattern, text)
        print("Фамилии с инициалами в тексте:")
        for name in initials:
            print(name)