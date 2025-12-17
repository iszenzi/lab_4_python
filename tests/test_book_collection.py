import pytest

from src.book import FictionBook, NonFictionBook
from src.collections import BookCollection


class TestBookCollection:
    """Тесты для класса BookCollection"""

    def test_add_book(self):
        collection = BookCollection()
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")
        collection.add_book(book)
        assert len(collection) == 1
        assert collection[0] == book

    def test_add_book_invalid_type_raises(self):
        collection = BookCollection()
        with pytest.raises(TypeError) as exc_info:
            collection.add_book("NotABook")
        assert str(exc_info.value) == "Можно добавлять только объекты Book"
        assert exc_info.type is TypeError

    def test_remove_book(self):
        book1 = FictionBook("Title1", "Author1", 2020, "Genre1", "987-4567890123")
        book2 = NonFictionBook("Title2", "Author2", 2019, "Genre2", "987-6543210987")
        collection = BookCollection([book1, book2])

        collection.remove_book(book1)
        assert len(collection) == 1
        assert collection[0] == book2

    def test_remove_book_invalid_type_raises(self):
        book = FictionBook("Title", "Author", 2020, "Genre", "987-4567890123")
        collection = BookCollection([book])
        with pytest.raises(TypeError) as exc_info:
            collection.remove_book("NotABook")
        assert str(exc_info.value) == "Можно удалять только объекты Book"
        assert exc_info.type is TypeError

    def test_remove_book_not_in_collection_raises(self):
        book1 = FictionBook("Title1", "Author1", 2020, "Genre1", "987-4567890123")
        book2 = NonFictionBook("Title2", "Author2", 2019, "Genre2", "987-6543210987")
        collection = BookCollection([book1])
        with pytest.raises(ValueError) as exc_info:
            collection.remove_book(book2)
        assert str(exc_info.value) == "Нельзя удалить книгу которой нет в коллекции"
        assert exc_info.type is ValueError

    def test_getitem(self):
        book1 = FictionBook("Title1", "Author1", 2020, "Genre1", "987-4567890123")
        book2 = NonFictionBook("Title2", "Author2", 2019, "Genre2", "987-6543210987")
        book3 = FictionBook("Title3", "Author3", 2018, "Genre3", "987-1234567890")
        collection = BookCollection([book1, book2, book3])
        slice_collection = collection[0:2]
        middle_book = slice_collection[1]
        assert len(slice_collection) == 2
        assert middle_book == book2

    def test_contains(self):
        book1 = FictionBook("Title1", "Author1", 2020, "Genre1", "987-4567890123")
        book2 = NonFictionBook("Title2", "Author2", 2019, "Genre2", "987-6543210987")
        collection = BookCollection([book1])
        assert book1 in collection
        assert book2 not in collection

    def test_iteration(self):
        book1 = FictionBook("Title1", "Author1", 2020, "Genre1", "987-4567890123")
        book2 = NonFictionBook("Title2", "Author2", 2019, "Genre2", "987-6543210987")
        collection = BookCollection([book1, book2])
        books = [book for book in collection]
        assert books == [book1, book2]
