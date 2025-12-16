# from __future__ import annotations

from typing import Union, Dict, Any

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

    def __iter__(self):
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
        self._indexes: Dict[str, Dict[Any, Any]] = {
            "isbn": {},
            "author": {},
            "year": {},
        }

    def add_book(self, book: Book) -> None:
        if book.isbn in self._indexes["isbn"]:
            raise ValueError(f"Книга с таким ISBN: '{book}' уже есть в коллекции")
        self._indexes["isbn"][book.isbn] = book
        self._indexes["author"].setdefault(book.author, []).append(book)
        self._indexes["year"].setdefault(book.year, []).append(book)

    def remove_book(self, book: Book) -> None:
        if book.isbn not in self._indexes["isbn"]:
            raise ValueError(f"Книги с таким ISBN: '{book}'  нет в коллекции")
        del self._indexes["isbn"][book.isbn]

        if book.author in self._indexes["author"]:
            self._indexes["author"][book.author].remove(book)
            if not self._indexes["author"][book.author]:
                del self._indexes["author"][book.author]

        if book.year in self._indexes["year"]:
            self._indexes["year"][book.year].remove(book)
            if not self._indexes["year"][book.year]:
                del self._indexes["year"][book.year]

    def __len__(self):
        return len(self._indexes["isbn"])

    def __iter__(self):
        return iter(self._indexes["isbn"].values())

    def __getitem__(self, key: Union[str, int]) -> Any:
        if isinstance(key, str):
            if key in self._indexes:
                return self._indexes[key]
            if key in self._indexes["isbn"]:
                return self._indexes["isbn"][key]
            if key in self._indexes["author"]:
                return self._indexes["author"][key]
        elif isinstance(key, int):
            if key in self._indexes["year"]:
                return self._indexes["year"][key]
        raise KeyError(f"Ключ '{key}' не найден")

    def __contains__(self, item: Union[Book, str, int]) -> bool:
        if isinstance(item, Book):
            return item.isbn in self._indexes["isbn"]
        elif isinstance(item, str):
            return item in self._indexes["isbn"] or item in self._indexes["author"]
        elif isinstance(item, int):
            return item in self._indexes["year"]
        return False
