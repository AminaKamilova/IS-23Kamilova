# Создайте базовый класс "Животное" со свойствами "вид", "количество лап",
# "цвет шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него
#  свойства "кличка" и "порода".
class Animal:
    def __init__(self, view, number_of_paws, coat_color):
        self.view = view
        self.number_of_paws = number_of_paws
        self.coat_color = coat_color

class Dog(Animal):
    def __init__(self, view, number_of_paws, coat_color, moniker, breed):
        super().__init__(view, number_of_paws, coat_color)
        self.moniker = moniker
        self.breed = breed

animal = Animal("Кошка", 4, "Черный")
dog = Dog("Собака", 4, "Коричневый", "Рекс", "Пудель")

print(dog.view)
print(dog.moniker)



