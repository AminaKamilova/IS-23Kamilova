class Note:
    def __init__(self, text, iscompleted: bool = False):
        self.text = text
        self.count = 0
        self.iscompleted = iscompleted

    def upcount(self):
        self.count += 10

    def reset_count(self):
        self.count = 0

note1 = Note("Задача1", True)
# print(note1)
# print(note1.__dict__)
# print(dir(note1))

# Привязанные методы
# print(note1.iscompleted()) # bound -  метод является приявязанным для экземпляра note1
print(note1.__dict__)
# print(Note.upcount()) # function - с точки зрения класса Note upcount является обычной функцией

note2 = Note("Задача2", False)
# # print(note1)
print(note2.__dict__)
# print(dir(note2))
# print(note2.text)

note3 = 4
print(note3.)


