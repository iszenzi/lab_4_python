from typing import Any, Dict, Iterator, Union

from src.book import Book


class BookCollection:
    def __init__(self, books: list[Book] | None = None):
        if books is None:
            self._books: list[Book] = []
        else:
            self._books = list(books)

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        self._books.remove(book)

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self) -> Iterator[Book]:
        return iter(self._books)

    def __getitem__(self, key: int | slice) -> Union[Book, "BookCollection"]:
        if isinstance(key, int):
            return self._books[key]
        elif isinstance(key, slice):
            return BookCollection(self._books[key])
        else:
            raise TypeError("Индекс должен быть целым числом или срезом")

    def __contains__(self, book: Book) -> bool:
        return book in self._books


class IndexDict:
    def __init__(self) -> None:
        self._by_isbn: Dict[str, Book] = {}
        self._by_author: Dict[str, BookCollection] = {}
        self._by_year: Dict[int, BookCollection] = {}

    def get_by_isbn(self, isbn: str) -> Book | None:
        return self._by_isbn.get(isbn)

    def get_by_author(self, author: str) -> BookCollection:
        return self._by_author.get(author, BookCollection())

    def get_by_year(self, year: int) -> BookCollection:
        return self._by_year.get(year, BookCollection())

    def add_book(self, book: Book) -> None:
        if book.isbn in self._by_isbn:
            raise ValueError(f"Книга с таким ISBN: '{book}' уже есть в коллекции")
        self._by_isbn[book.isbn] = book
        self._by_author.setdefault(book.author, BookCollection()).add_book(book)
        self._by_year.setdefault(book.year, BookCollection()).add_book(book)

    def remove_book(self, book: Book) -> None:
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

    def __len__(self):
        return len(self._by_isbn)

    def __iter__(self):
        return iter(self._by_isbn.values())

    def __getitem__(self, key: Union[str, int]) -> Any:
        """Доступ по ключу.

        Поддерживается:
        - `str`: сначала трактуется как ISBN, затем как author.
        - `int`: трактуется как year.

        Примечание: строковый ключ неоднозначен (ISBN/author). На следующем этапе
        сделаем API явным и избавимся от этой неоднозначности.
        """

        if isinstance(key, str):
            if key in self._by_isbn:
                return self._by_isbn[key]
            if key in self._by_author:
                return self._by_author[key]
        elif isinstance(key, int):
            if key in self._by_year:
                return self._by_year[key]
        raise KeyError(f"Ключ '{key}' не найден")

    def __contains__(self, item: Union[Book, str, int]) -> bool:
        if isinstance(item, Book):
            return item.isbn in self._by_isbn
        elif isinstance(item, str):
            return item in self._by_isbn or item in self._by_author
        elif isinstance(item, int):
            return item in self._by_year
        return False
