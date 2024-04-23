class Comment:
    def __int__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"

my_comment = Comment("My")

m_1 = Comment.merge_comments("Hi", "student")
print(m_1)
m_2 = Comment.merge_comments("Great", "Ok")
print(m_2)

class Comment:
    count = 0

    def __init__(self, text):
        self.text = text

    def upcount(self):
        self.count += 1

my_comment = Comment("My comment")

#####
######
