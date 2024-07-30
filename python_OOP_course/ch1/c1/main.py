class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        # print(f'searching for book to remove: {book}')
        for lib_b in self.books:
            if lib_b.title == book.title and lib_b.author == book.author:
                # print(f'book to be remove: {book}')
                self.books.remove(lib_b)

    def search_books(self, search_string):
        found_book = []
        for book in self.books:
            # print(f'{book}  title: {book.title} author: {book.author}')
            # print(search_string)
            if (search_string in book.title.lower()
                    or search_string in book.author.lower()):
                # print(f'found book: {book.title}')
                found_book.append(book)
        return found_book
