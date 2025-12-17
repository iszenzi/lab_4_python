import random
from typing import Callable

from src.book import Book, FictionBook, NonFictionBook
from src.collections import IndexDict
from src.library import Library
from src.exceptions import SimulationError


def generate_random_book() -> Book:
    """
    Генерирует случайную книгу
    :return: Сгенерированная книга
    """
    titles = [
        "Утиные истории",
        "Случайная книга",
        "Конкретная математика",
        "Фантастические твари и где они обитают",
        "Гарри Поттер и философский камень",
        "Гарри Поттер и тайная комната",
        "Сборник задач и упражнений по математическому анализу",
        "Война и мир",
        "Капитанская дочка",
        "Евгений Онегин",
        "Преступление и наказание",
    ]
    authors = [
        "Карл Баркс",
        "Иван Иванов",
        "Дональд Кнут",
        "Дж. К. Роулинг",
        "Б.П. Демидович",
        "Л.Н.Толстой",
        "А.С. Пушкин",
        "Ф.М. Достоевский",
    ]
    years = list(range(1900, 2025))
    genres = [
        "Комикс",
        "Математика",
        "Фентези",
        "Роман",
        "Роман-эпопея",
    ]
    isbns = [f"978-{random.randint(1000000000, 9999999999)}" for _ in range(10)]

    title = random.choice(titles)
    author = random.choice(authors)
    year = random.choice(years)
    genre = random.choice(genres)
    isbn = random.choice(isbns)

    if genre == "Математика":
        return NonFictionBook(title, author, year, genre, isbn)
    else:
        return FictionBook(title, author, year, genre, isbn)


def add_random_book(library: Library) -> None:
    """
    Добавляет случайную книгу в библиотеку
    :param library: Библиотека
    :return: None
    """
    book = generate_random_book()
    try:
        library.add_book(book)
        print(f"Добавлена книга: {book}")
    except Exception as exc:
        raise SimulationError(f"Не удалось добавить книгу {book}, ошибка: {exc}")


def remove_random_book(library: Library) -> None:
    """
    Удаляет случайную книгу из библиотеки
    :param library: Библиотека
    :return: None
    """
    if len(library.collection) == 0:
        raise SimulationError("Коллекция пустая")

    book = random.choice(list(library.collection))
    try:
        library.remove_book(book)
        print(f"Удалена книга: {book}")
    except Exception as exc:
        raise SimulationError(f"Не удалось удалить книгу {book}, ошибка: {exc}")


def search_by_author(library: Library, author: str | None = None) -> list[Book]:
    """
    Ищет книги по автору
    :param library: Библиотека
    :param author: Автор
    :return: Список найденных книг
    """
    author_index = library.index["author"]
    if author is None:
        if not author_index:
            raise SimulationError("Нет авторов для поиска")
        author = random.choice(list(author_index.keys()))

    found = library.find_by_author(author)
    result = list(found)
    print(f"По автору '{author}' найдено {len(result)} книг")
    for book in result:
        print(book)
    return result


def search_by_year(library: Library, year: int | None = None) -> list[Book]:
    """
    Ищет книги по году
    :param library: Библиотека
    :param year: Год
    :return: Список найденных книг
    """
    year_index = library.index["year"]
    if year is None:
        if not year_index:
            raise SimulationError("Нет годов для поиска")
        year = random.choice(list(year_index.keys()))

    found = library.find_by_year(year)
    result = list(found)
    print(f"По году {year} найдено {len(result)} книг")
    for book in result:
        print(book)
    return result


def search_by_genre(library: Library, genre: str | None = None) -> list[Book]:
    """
    Ищет книги по жанру
    :param library: Библиотека
    :param genre: Жанр
    :return: Список найденных книг
    """
    if genre is None:
        genres = [book.genre for book in library.collection]
        if not genres:
            raise SimulationError("Нет жанров для поиска")
        genre = random.choice(genres)

    found = library.find_by_genre(genre)
    result = list(found)
    print(f"По жанру '{genre}' найдено {len(result)} книг")
    for book in result:
        print(book)
    return result


def update_index(library: Library) -> None:
    """
    Обновляет индекс библиотеки
    :param library: Библиотека
    :return: None
    """
    new_index = IndexDict()
    try:
        for book in library.collection:
            new_index.add_book(book)
    except Exception as exc:
        raise SimulationError(f"Не удалось обновить индекс, ошибка: {exc}")

    library.index = new_index
    print(f"Индекс обновлён, {len(library.index)} книг в индексе")


def get_nonexistent_book(library: Library) -> None:
    """
    Проверяет несуществующую книгу в библиотеке
    :param library: Библиотека
    :return: None
    """
    isbn_index = library.index["isbn"]

    fake_isbn = ""
    while True:
        fake_isbn = f"978-{random.randint(1000000000, 9999999999)}"
        if fake_isbn not in isbn_index:
            break
    book = library.find_by_isbn(fake_isbn)
    if book is not None:
        raise SimulationError(f"Неожиданно найдена книга с ISBN '{fake_isbn}': {book}")
    print(f"Книга с несуществующим ISBN '{fake_isbn}' не найдена")


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Запускает симуляцию библиотеки, выбирая одно случайное событие
    :param steps: Количество шагов симуляции
    :param seed: сид для генератора случайных событий
    :return: None
    """
    if seed is not None:
        random.seed(seed)
    library = Library()

    print("Добавление начальных книг в библиотеку:")
    for _ in range(5):
        add_random_book(library)

    events: list[tuple[str, Callable]] = [
        ("add_book", lambda: add_random_book(library)),
        ("remove_book", lambda: remove_random_book(library)),
        ("search_author", lambda: search_by_author(library)),
        ("search_year", lambda: search_by_year(library)),
        ("search_genre", lambda: search_by_genre(library)),
        ("update_index", lambda: update_index(library)),
        ("get_nonexistent", lambda: get_nonexistent_book(library)),
    ]

    print(f"НАЧАЛО СИМУЛЯЦИИ шагов {steps}, сид {seed}")
    for step in range(1, steps + 1):
        event_name, event_fn = random.choice(events)
        print(
            f"\n[шаг {step}/{steps}] событие {event_name}, {len(library.collection)} книг в библиотеке"
        )
        try:
            event_fn()
        except SimulationError as exc:
            print(f"[шаг {step}/{steps}] событие {event_name} ОШИБКА: {exc}")

    print(f"\nКОНЕЦ СИМУЛЯЦИИ всего книг в библиотеке {len(library.collection)}")
