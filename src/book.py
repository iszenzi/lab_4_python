class Book:
    """Базовый класс книги"""

    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        """
        Создает объект книги
        :param title: Название
        :param author: Автор
        :param year: Год
        :param genre: Жанр
        :param isbn: ISBN
        :return: None
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        """
        Возвращает книгу в строковом виде
        :return: Строка с полями книги
        """
        return f'Book(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'


class FictionBook(Book):
    """Книга художественного типа"""

    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        """
        Создает художественную книгу
        :param title: Название
        :param author: Автор
        :param year: Год
        :param genre: Жанр
        :param isbn: ISBN
        :return: None
        """
        super().__init__(title, author, year, genre, isbn)

    def __repr__(self) -> str:
        """
        Возвращает художественную книгу в строковом виде
        :return: Строка с полями книги
        """
        return f'FictionBook(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'


class NonFictionBook(Book):
    """Книга нехудожественного типа"""

    def __init__(
        self, title: str, author: str, year: int, genre: str, isbn: str
    ) -> None:
        """
        Создает нехудожественную книгу
        :param title: Название
        :param author: Автор
        :param year: Год
        :param genre: Жанр
        :param isbn: ISBN
        :return: None
        """
        super().__init__(title, author, year, genre, isbn)

    def __repr__(self) -> str:
        """
        Возвращает нехудожественную книгу в строковом виде
        :return: Строка с полями книги
        """
        return f'NonFictionBook(title="{self.title}", author="{self.author}", year={self.year}, genre="{self.genre}", isbn="{self.isbn}")'
