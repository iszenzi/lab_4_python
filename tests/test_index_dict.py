import pytest

from src.book import FictionBook, NonFictionBook
from src.collections import BookCollection, IndexDict


class TestIndexDict:
    """Тесты для класса IndexDict"""

    def test_add_book(self):
        index = IndexDict()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")

        index.add_book(book)

        assert len(index) == 1
        assert book in index
        assert book.isbn in index
        assert book.author in index
        assert book.year in index

        isbn_index = index["isbn"]
        author_index = index["author"]
        year_index = index["year"]

        assert isbn_index[book.isbn] == book
        assert isinstance(author_index[book.author], BookCollection)
        assert list(author_index[book.author]) == [book]
        assert isinstance(year_index[book.year], BookCollection)
        assert list(year_index[book.year]) == [book]

    def test_add_book_invalid_type_raises(self):
        index = IndexDict()
        with pytest.raises(TypeError) as exc_info:
            index.add_book("NotABook")
        assert str(exc_info.value) == "Можно добавлять только объекты Book"
        assert exc_info.type is TypeError

    def test_add_book_duplicate_raises(self):
        index = IndexDict()
        book1 = FictionBook("Title1", "Author", 2020, "Genre", "987-4567890123")
        book2 = NonFictionBook("Title2", "Other", 2019, "Математика", "987-4567890123")

        index.add_book(book1)
        with pytest.raises(ValueError) as exc_info:
            index.add_book(book2)

        assert (
            str(exc_info.value) == f"Книга с таким ISBN: '{book2}' уже есть в коллекции"
        )
        assert exc_info.type is ValueError

    def test_remove_book(self):
        index = IndexDict()
        book1 = FictionBook("Title1", "Author", 2020, "Genre", "987-4567890123")
        book2 = FictionBook("Title2", "Author", 2021, "Genre", "987-6543210987")

        index.add_book(book1)
        index.add_book(book2)

        index.remove_book(book1)
        assert len(index) == 1
        assert book1 not in index
        assert book1.isbn not in index
        assert book1.year not in index
        assert book1.author in index

        index.remove_book(book2)
        assert len(index) == 0
        assert book2 not in index
        assert book2.isbn not in index
        assert book2.author not in index
        assert book2.year not in index

    def test_remove_book_invalid_type_raises(self):
        index = IndexDict()
        with pytest.raises(TypeError) as exc_info:
            index.remove_book("NotABook")
        assert str(exc_info.value) == "Можно удалять только объекты Book"
        assert exc_info.type is TypeError

    def test_remove_book_not_in_index_raises(self):
        index = IndexDict()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")
        with pytest.raises(ValueError) as exc_info:
            index.remove_book(book)

        assert str(exc_info.value) == f"Книги с таким ISBN: '{book}'  нет в коллекции"
        assert exc_info.type is ValueError

    def test_getitem_unknown_key_raises(self):
        index = IndexDict()
        with pytest.raises(KeyError) as exc_info:
            index["unknown"]
        assert exc_info.value.args[0] == "Ключ 'unknown' не найден"
        assert exc_info.type is KeyError

    def test_iter_returns_books(self):
        index = IndexDict()
        book1 = FictionBook("Title1", "Author1", 2020, "Genre", "987-4567890123")
        book2 = FictionBook("Title2", "Author2", 2021, "Genre", "987-6543210987")

        index.add_book(book1)
        index.add_book(book2)

        assert list(index) == [book1, book2]
