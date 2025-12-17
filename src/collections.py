from typing import Any, Dict, Iterator

from src.book import Book


class BookCollection:
    """Пользовательская списковая коллекция книг"""

    def __init__(self, books: list[Book] | None = None) -> None:
        """
        Создает коллекцию книг
        :param books: Начальный список книг
        :return: None
        """
        if books is None:
            self._books: list[Book] = []
        else:
            self._books = list(books)

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу в коллекцию
        :param book: Книга
        :return: None
        """
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        """
        Удаляет книгу из коллекции
        :param book: Книга
        :return: None
        """
        self._books.remove(book)

    def __len__(self) -> int:
        """
        Возвращает количество книг
        :return: Количество книг
        """
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:
        """
        Делает коллекцию итерируемой
        :return: Итератор по книгам
        """
        return iter(self._books)

    def __getitem__(self, key: int | slice) -> Book | "BookCollection":
        """
        Возвращает книгу по индексу или подколлекцию по срезу
        :param key: Индекс или срез
        :return: Книга или новая коллекция
        """
        if isinstance(key, int):
            return self._books[key]
        elif isinstance(key, slice):
            return BookCollection(self._books[key])
        else:
            raise TypeError("Индекс должен быть целым числом или срезом")

    def __contains__(self, book: Book) -> bool:
        """
        Проверяет наличие книги в коллекции
        :param book: Книга
        :return: True если книга есть, иначе False
        """
        return book in self._books


class IndexDict:
    """Пользовательская словарная коллекция индексов"""

    def __init__(self) -> None:
        """
        Создает пустые индексы
        :return: None
        """
        self._by_isbn: Dict[str, Book] = {}
        self._by_author: Dict[str, BookCollection] = {}
        self._by_year: Dict[int, BookCollection] = {}

    def add_book(self, book: Book) -> None:
        """
        Добавляет книгу
        :param book: Книга
        :return: None
        """
        if book.isbn in self._by_isbn:
            raise ValueError(f"Книга с таким ISBN: '{book}' уже есть в коллекции")
        self._by_isbn[book.isbn] = book
        self._by_author.setdefault(book.author, BookCollection()).add_book(book)
        self._by_year.setdefault(book.year, BookCollection()).add_book(book)

    def remove_book(self, book: Book) -> None:
        """
        Удаляет книгу
        :param book: Книга
        :return: None
        """
        if book.isbn not in self._by_isbn:
            raise ValueError(f"Книги с таким ISBN: '{book}'  нет в коллекции")
        del self._by_isbn[book.isbn]

        if book.author in self._by_author:
            self._by_author[book.author].remove_book(book)
            if not self._by_author[book.author]:
                del self._by_author[book.author]

        if book.year in self._by_year:
            self._by_year[book.year].remove_book(book)
            if not self._by_year[book.year]:
                del self._by_year[book.year]

    def __len__(self) -> int:
        """
        Возвращает количество книг в индексе по ISBN
        :return: Количество книг
        """
        return len(self._by_isbn)

    def __iter__(self) -> Iterator[Book]:
        """
        Итерирование по книгам в индексе ISBN
        :return: Итератор по книгам
        """
        return iter(self._by_isbn.values())

    def __getitem__(self, key: str | int) -> Any:
        """
        Доступ к индексам или к элементам по ключу
        :param key: "isbn" "author" "year" или конкретный ключ
        :return: Словарь индекса или книга или коллекция
        """
        if key == "isbn":
            return self._by_isbn
        if key == "author":
            return self._by_author
        if key == "year":
            return self._by_year

        if isinstance(key, str):
            if key in self._by_isbn:
                return self._by_isbn[key]
            if key in self._by_author:
                return self._by_author[key]
        elif isinstance(key, int):
            if key in self._by_year:
                return self._by_year[key]

        raise KeyError(f"Ключ '{key}' не найден")

    def __contains__(self, item: Book | str | int) -> bool:
        """
        Проверяет наличие книги или ключа в индексах
        :param item: Книга или ключ
        :return: True если найдено, иначе False
        """
        if isinstance(item, Book):
            return item.isbn in self._by_isbn
        elif isinstance(item, str):
            return item in self._by_isbn or item in self._by_author
        elif isinstance(item, int):
            return item in self._by_year
        return False
