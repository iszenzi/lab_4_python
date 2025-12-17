from src.book import Book
from src.collections import BookCollection, IndexDict


class Library:
    """Класс библиотеки"""

    def __init__(self) -> None:
        """
        Создает пустую библиотеку
        :return: None
        """
        self.collection = BookCollection()
        self.index = IndexDict()

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу в библиотеку и индекс
        :param book: Книга
        :return: None
        """
        self.index.add_book(book)
        self.collection.add_book(book)

    def remove_book(self, book: Book) -> None:
        """
        Удаляет книгу из библиотеки и индекса
        :param book: Книга
        :return: None
        """
        self.collection.remove_book(book)
        self.index.remove_book(book)

    def find_by_isbn(self, isbn: str) -> Book | None:
        """
        Ищет книгу по ISBN
        :param isbn: ISBN книги
        :return: Книга или None
        """
        isbn_index = self.index["isbn"]
        return isbn_index.get(isbn)

    def find_by_author(self, author: str) -> BookCollection:
        """
        Ищет книги по автору
        :param author: Автор
        :return: Коллекция найденных книг
        """
        author_index = self.index["author"]
        return BookCollection(list(author_index.get(author, BookCollection())))

    def find_by_year(self, year: int) -> BookCollection:
        """
        Ищет книги по году
        :param year: Год
        :return: Коллекция найденных книг
        """
        year_index = self.index["year"]
        return BookCollection(list(year_index.get(year, BookCollection())))

    def find_by_genre(self, genre: str) -> BookCollection:
        """
        Ищет книги по жанру
        :param genre: Жанр
        :return: Коллекция найденных книг
        """
        result = BookCollection()
        for book in self.collection:
            if book.genre == genre:
                result.add_book(book)
        return result

    def __repr__(self) -> str:
        """
        Возвращает библиотеку в строковом виде
        :return: Строковый вид библиотеки
        """
        return f"Library(books_count={len(self.collection)})"
