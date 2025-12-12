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

    def __getitem__(self, key: int | slice):
        if isinstance(key, int):
            return self._books[key]
        elif isinstance(key, slice):
            return BookCollection(self._books[key])
        else:
            raise TypeError("Индекс должен быть целым числом или срезом")

    def __contains__(self, book: Book) -> bool:
        return book in self._books
