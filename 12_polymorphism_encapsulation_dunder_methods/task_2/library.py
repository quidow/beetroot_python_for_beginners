class Author:

    def __init__(self, name, country, birthday):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(country, str):
            raise TypeError
        if not isinstance(birthday, int):
            raise TypeError
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError
        if book not in self.books:
            self.books.append(book)

    def __eq__(self, other):
        if not isinstance(other, Author):
            raise TypeError
        if (
                self.name == other.name
                and self.country == other.country
                and self.birthday == other.birthday
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"<Author: {self.name}>"

    def __str__(self):
        return f"{self.name}"


class Book:
    books = []

    def __init__(self, name, year, author):
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError
        if not isinstance(author, Author):
            raise TypeError
        self.name = name
        self.year = year
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise TypeError
        if (
                self.name == other.name
                and self.year == other.year
                and self.author == other.author
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"<Book: {self.name}>"

    def __str__(self):
        return f"{self.name}"


class Library:

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        if book not in self.books:
            self.books.append(book)
        if book not in Book.books:
            Book.books.append(book)
        if author not in self.authors:
            self.authors.append(author)

    def group_by_author(self, author):
        if not isinstance(author, Author):
            raise TypeError
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        if isinstance(year, int):
            raise TypeError
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"<Library: {self.name}>"

    def __str__(self):
        return f"{self.name}"
