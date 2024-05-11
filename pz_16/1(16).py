class Building:
    def address(self):
        input("Введите адрес: ")
    def number_of_floors(self):
        int(input("Введите количество этажей: "))

    @staticmethod
    def conclusion(text, count):
        return f"{text} {count}"


address = Building()
number_of_floors = Building()
address.address()
number_of_floors.number_of_floors()
