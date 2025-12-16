class Book:
    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        return f'Book(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'


class FictionBook(Book):
    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        super().__init__(title, author, year, genre, isbn)

    def __repr__(self) -> str:
        return f'FictionBook(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'


class NonFictionBook(Book):
    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        super().__init__(title, author, year, genre, isbn)

    def __repr__(self) -> str:
        return f'NonFictionBook(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'
