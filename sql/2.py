class Note:
    def __init__(self,text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1

note1 = Note("Задача1")
note2 = Note("Задача2")
