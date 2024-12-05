zoznam = [1, 2, 3, 4, 5, 6, 7]

list_iterator = iter(zoznam)
list_iterator1 = iter(zoznam)
# print(next(list_iterator))
# print(next(list_iterator1))

slovnik = {1: "a", 2: "b", 3: "c"}

slovnik_iterator = iter(slovnik)
# print(next(slovnik_iterator))
# print(next(slovnik_iterator))

moj_string = "Hello World"

string_iterator = iter(moj_string)
print(next(string_iterator))
print(next(string_iterator))


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return self.__dict__


class BookCollection:
    def __init__(self):
        self.books = []
        self.index = 0

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

collection = BookCollection()
collection.add_book(book1)
collection.add_book(book2)
collection.add_book(book3)

iter1 = iter(collection)
iter2 = iter(collection)

# print(next(iter1))
# print(next(iter2))
