myList = [1,2,3]
print(len(myList))

class Sample():
    pass
mysample = Sample()

print(mysample)
print(myList)

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book('Python from scratch', 'O\'relly', 500)
print(b)
print(str(b))