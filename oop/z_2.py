class Person:
    count = 0

    def __init__(self):
        self.count += 1

    @staticmethod
    def total_people(text, count):
        return f"{text} {count}"


m_1 = Person.count
m_2 = Person.total_people("Количество экземпляров:", m_1)
print(m_2)
