# Создайте класс "Здание" с атрибутами "адрес" и "количество этажей".
# Напишите метод, который выводит информацию о здании в формате
# "Адрес: адрес, Количество этажей: этажи".

# Для задачи из блока 1 создать две функции, save_def u load_def, которые
# позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и
# загружать ее обратно. Использовать модуль pickle для сериализации и
# десериализации объектов Python в бинарном формате

import pickle

def save_def(filename, *objects, ):
    with open(filename, "wb") as f:
        pickle.dump(objects, f)

def load_def(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

class Building:
    def __init__(self, address, number_of_floors):
        self.address = address
        self.number_of_floors = number_of_floors

    @staticmethod
    def conclusion(text, count):
        return f"{text} {count}"

    def __str__(self):
        return f"Адрес: {self.address}, Количество этажей: {self.number_of_floors}"

building1 = Building(input("Введите адрес №1: "), input("Введите количество этажей: "))
building2 = Building(input("Введите адрес №2: "), input("Введите количество этажей: "))
building3 = Building(input("Введите адрес №3: "), input("Введите количество этажей: "))
save_def("buildings.pkl", building1, building2, building3)
buildings = load_def("buildings.pkl")

for building in buildings:
    print("\n", building)
