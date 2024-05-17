# Создайте класс "Здание" с атрибутами "адрес" и "количество этажей".
# Напишите метод, который выводит информацию о здании в формате
# "Адрес: адрес, Количество этажей: этажи".

# Для задачи из блока 1 создать две функции, save_def u load_def, которые
# позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и
# загружать ее обратно. Использовать модуль pickle для сериализации и
# десериализации объектов Python в бинарном формате
import pickle

def save_def(filename, *objects):
    """Сохраняет объекты в файл в бинарном формате с помощью pickle."""

    with open(filename, "wb") as f:
        pickle.dump(objects, f)

def load_def(filename):
    """Загружает объекты из файла в бинарном формате с помощью pickle."""

    with open(filename, "rb") as f:
        return pickle.load(f)
class Building:
    def address():
        address = input("Введите адрес: ")
        return address

    def number_of_floors():
        number_of_floors = input("Введите количество этажей: ")
        while int != type(number_of_floors):
            try:
                number_of_floors = int(number_of_floors)
            except ValueError:
                number_of_floors = input("Введите количество этажей: ")
        return number_of_floors

    @staticmethod
    def conclusion(text, count):
        return f"{text} {count}"


address_value = Building.address()
number_of_floors_value = Building.number_of_floors()
print()
print(Building.conclusion("Адрес:", address_value))
print(Building.conclusion("Количество этажей:", number_of_floors_value))


save_def("buildings.pkl", building1, building2, building3)
buildings = load_def("buildings.pkl")