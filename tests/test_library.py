import pytest

from src.book import FictionBook
from src.library import Library


class TestLibrary:
    """Тесты для класса Library"""

    def test_add_book_adds_to_collection_and_index(self):
        library = Library()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")

        library.add_book(book)

        assert len(library.collection) == 1
        assert library.collection[0] == book
        assert library.find_by_isbn(book.isbn) == book
        assert book in library.index

    def test_remove_book_removes_from_collection_and_index(self):
        library = Library()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")
        library.add_book(book)

        library.remove_book(book)

        assert len(library.collection) == 0
        assert library.find_by_isbn(book.isbn) is None
        assert book not in library.index
        assert book not in library.collection

    def test_remove_book_not_in_collection_raises(self):
        library = Library()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")

        with pytest.raises(ValueError) as exc_info:
            library.remove_book(book)

        assert str(exc_info.value) == "Нельзя удалить книгу которой нет в коллекции"
        assert exc_info.type is ValueError

    def test_find_by_author_returns_new_collection(self):
        library = Library()
        book1 = FictionBook("Title1", "Author", 2020, "Genre", "987-4567890123")
        book2 = FictionBook("Title2", "Author", 2021, "Genre", "987-6543210987")
        library.add_book(book1)
        library.add_book(book2)

        found = library.find_by_author("Author")
        assert list(found) == [book1, book2]

        found.add_book(FictionBook("Extra", "Author", 2022, "Genre", "987-0000000000"))
        assert list(library.find_by_author("Author")) == [book1, book2]

    def test_find_by_year(self):
        library = Library()
        book1 = FictionBook("Title1", "Author", 2020, "Genre", "987-4567890123")
        book2 = FictionBook("Title2", "Author", 2021, "Genre", "987-6543210987")
        library.add_book(book1)
        library.add_book(book2)

        assert list(library.find_by_year(2020)) == [book1]
        assert list(library.find_by_year(2021)) == [book2]
        assert list(library.find_by_year(1999)) == []

    def test_find_by_genre(self):
        library = Library()
        book1 = FictionBook("Title1", "Author", 2020, "Комикс", "987-4567890123")
        book2 = FictionBook("Title2", "Author", 2021, "Роман", "987-6543210987")
        book3 = FictionBook("Title3", "Author", 2022, "Комикс", "987-1234567890")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        assert list(library.find_by_genre("Комикс")) == [book1, book3]
        assert list(library.find_by_genre("Роман")) == [book2]
        assert list(library.find_by_genre("Фентези")) == []
