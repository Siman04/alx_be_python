class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        # This line must be indented and must accept (self, title, author)
        new_book = Book(title, author)
        self._books.append(new_book)

    def _find_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self._find_book(title)
        if book:
            return book.check_out()
        return False

    def return_book(self, title):
        book = self._find_book(title)
        if book:
            return book.return_book()
        return False

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)