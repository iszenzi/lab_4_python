from src.book import Book
from src.collections import BookCollection, IndexDict


class Library:
    def __init__(self) -> None:
        self.collection = BookCollection()
        self.index = IndexDict()

    def add_book(self, book: Book) -> None:
        self.index.add_book(book)
        self.collection.add_book(book)

    def remove_book(self, book: Book) -> None:
        self.collection.remove_book(book)
        self.index.remove_book(book)

    def find_by_isbn(self, isbn: str) -> Book | None:
        isbn_index = self.index["isbn"]
        return isbn_index.get(isbn)

    def find_by_author(self, author: str) -> BookCollection:
        author_index = self.index["author"]
        return BookCollection(list(author_index.get(author, BookCollection())))

    def find_by_year(self, year: int) -> BookCollection:
        year_index = self.index["year"]
        return BookCollection(list(year_index.get(year, BookCollection())))

    def find_by_genre(self, genre: str) -> BookCollection:
        result = BookCollection()
        for book in self.collection:
            if book.genre == genre:
                result.add_book(book)
        return result

    def __repr__(self) -> str:
        return f"Library(books_count={len(self.collection)})"
