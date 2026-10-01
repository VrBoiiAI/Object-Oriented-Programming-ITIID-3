# Create a class Book with attributes title and num_pages. Override:
#   __str__() to print "Book: X, Pages: Y".
#   __len__() so that len(book) returns the number of pages.

class Book:
    def __init__(self, title, num_pages):
        self.title = title
        self.num_pages = num_pages

    def __str__(self):
        return f'Book: {self.title}, Pages: {self.num_pages}'

    def __len__(self):
        return self.num_pages

book1 = Book("1984", 328)
print(book1)
print(len(book1))