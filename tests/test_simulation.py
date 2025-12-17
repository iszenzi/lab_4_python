import random

import pytest

from src.book import FictionBook, NonFictionBook
from src.collections import IndexDict
from src.exceptions import SimulationError
from src.library import Library
from src.simulation import (
    get_nonexistent_book,
    remove_random_book,
    search_by_author,
    search_by_genre,
    search_by_year,
    update_index,
)


class TestSimulation:
    """Тесты для симуляции"""

    def test_search_by_author(self, capsys):
        library = Library()
        book1 = FictionBook("T1", "Author", 2020, "Комикс", "987-4567890123")
        book2 = NonFictionBook("T2", "Author", 2021, "Математика", "987-4567890124")
        book3 = FictionBook("T3", "Other", 2022, "Роман", "987-4567890125")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        result = search_by_author(library, author="Author")

        out = capsys.readouterr().out
        assert result == [book1, book2]
        assert "По автору 'Author' найдено 2 книг" in out

    def test_search_by_year(self, capsys):
        library = Library()
        book1 = FictionBook("T1", "A1", 2020, "Комикс", "987-4567890123")
        book2 = FictionBook("T2", "A2", 2021, "Роман", "987-4567890124")
        library.add_book(book1)
        library.add_book(book2)

        result = search_by_year(library, year=2020)

        out = capsys.readouterr().out
        assert result == [book1]
        assert "По году 2020 найдено 1 книг" in out

    def test_search_by_genre(self, capsys):
        library = Library()
        book1 = FictionBook("T1", "A1", 2020, "Комикс", "987-4567890123")
        book2 = FictionBook("T2", "A2", 2021, "Роман", "987-4567890124")
        book3 = FictionBook("T3", "A3", 2022, "Комикс", "987-4567890125")
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        result = search_by_genre(library, genre="Комикс")

        out = capsys.readouterr().out
        assert result == [book1, book3]
        assert "По жанру 'Комикс' найдено 2 книг" in out

    def test_search_by_author_without_authors_raises(self):
        library = Library()
        with pytest.raises(SimulationError) as exc_info:
            search_by_author(library)
        assert str(exc_info.value) == "Нет авторов для поиска"

    def test_search_by_year_without_years_raises(self):
        library = Library()
        with pytest.raises(SimulationError) as exc_info:
            search_by_year(library)
        assert str(exc_info.value) == "Нет годов для поиска"

    def test_search_by_genre_without_genres_raises(self):
        library = Library()
        with pytest.raises(SimulationError) as exc_info:
            search_by_genre(library)
        assert str(exc_info.value) == "Нет жанров для поиска"

    def test_update_index(self, capsys):
        library = Library()
        book1 = FictionBook("T1", "A1", 2020, "Комикс", "987-4567890123")
        book2 = FictionBook("T2", "A2", 2021, "Роман", "987-4567890124")
        library.add_book(book1)
        library.add_book(book2)

        library.index = IndexDict()
        assert library.find_by_isbn(book1.isbn) is None

        update_index(library)

        out = capsys.readouterr().out
        assert library.find_by_isbn(book1.isbn) == book1
        assert len(library.index) == 2
        assert "Индекс обновлён" in out

    def test_get_nonexistent_book_does_not_raise(self, capsys):
        random.seed(1)
        library = Library()
        book = FictionBook("T1", "A1", 2020, "Комикс", "987-4567890123")
        library.add_book(book)

        get_nonexistent_book(library)

        out = capsys.readouterr().out
        assert "не найдена" in out

    def test_remove_random_book_empty_raises(self):
        library = Library()
        with pytest.raises(SimulationError) as exc_info:
            remove_random_book(library)
        assert str(exc_info.value) == "Коллекция пустая"
