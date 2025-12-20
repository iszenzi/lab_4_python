# Лабораторная работа №4 - Библиотека

## Описание
Этот проект представляет систему управления библиотекой на Python. В проекте есть базовые классы книг, пользовательская коллекция книг, пользовательские индексы для ускорения поиска, библиотека с методами поиска и симуляция случайных событий.

## Структура проекта
```text
|-- src/
|   |-- __init__.py
|   |-- book.py          # Классы книг
|   |-- collections.py   # Пользовательские коллекции BookCollection и IndexDict
|   |-- exceptions.py    # Исключения
|   |-- library.py       # Класс Library
|   |-- main.py          # CLI для запуска симуляции
|   |-- simulation.py    # Симуляция случайных событий
|
|-- tests/
|   |-- __init__.py
|   |-- test_book_collection.py  # Тесты BookCollection
|   |-- test_index_dict.py       # Тесты IndexDict
|   |-- test_library.py          # Тесты Library
|   |-- test_simulation.py       # Тесты функций симуляции
|
|-- .gitignore           # Игнорируемые файлы/папки
|-- pyproject.toml
|-- requirements.txt     # Зависимости для pip install
|-- .pre-commit-config.yaml
|-- uv.lock
|-- README.md            # Описание лабораторной
```

## Реализованные компоненты

### Книги
- `Book` - базовый класс книги
	- `__init__(title: str, author: str, year: int, genre: str, isbn: str)`
		- `title`: название книги
		- `author`: автор книги
		- `year`: год издания
		- `genre`: жанр
		- `isbn`: ISBN
	- `__repr__() -> str` — строковое представление книги
- `FictionBook` - художественная книга
	- `__init__(title: str, author: str, year: int, genre: str, isbn: str)`
		- `title`: название книги
		- `author`: автор книги
		- `year`: год издания
		- `genre`: жанр
		- `isbn`: ISBN
	- `__repr__() -> str` — строковое представление художественной книги
- `NonFictionBook` - нехудожественная книга
	- `__init__(title: str, author: str, year: int, genre: str, isbn: str)`
		- `title`: название книги
		- `author`: автор книги
		- `year`: год издания
		- `genre`: жанр
		- `isbn`: ISBN
	- `__repr__() -> str` — строковое представление нехудожественной книги

### Пользовательские коллекции

BookCollection
Методы:
- `__init__(books: list[Book] | None = None)` - создание коллекции
	- `books`: начальный список книг (или `None` для пустой коллекции)
- `add_book(book: Book)` - добавление книги в коллекцию
	- `book`: добавляемая книга
- `remove_book(book: Book)` - удаление книги из коллекции
	- `book`: удаляемая книга
- `__len__()` - количество книг в коллекции
- `__iter__()` - итерация по книгам
- `__getitem__(key: int | slice)` - доступ по индексу и срезу
	- `key`: индекс (`int`) или срез (`slice`)
- `__contains__(book: Book)` - проверка наличия книги в коллекции
	- `book`: книга для проверки

IndexDict
Методы:
- `__init__()` - создание пустых индексов
- `add_book(book: Book)` - добавление книги в индексы
	- `book`: добавляемая книга
- `remove_book(book: Book)` - удаление книги из индексов
	- `book`: удаляемая книга
- `__len__()` - количество книг в индексе по ISBN
- `__iter__()` - итерация по книгам в индексе ISBN
- `__getitem__(key: str | int)` - доступ к индексам и поиск по ключу
	- `key`: один из литералов (`"isbn"`, `"author"`, `"year"`) или конкретный ключ поиска (ISBN/автор/год)
- `__contains__(item: Book | str | int)` - проверка наличия книги или ключа в индексах
	- `item`: книга (`Book`) или ключ (ISBN `str`, автор `str`, год `int`)

### Библиотека

Library
Методы:
- `__init__()` - создание пустой библиотеки
- `add_book(book: Book)` - добавление книги в библиотеку и индекс
	- `book`: добавляемая книга
- `remove_book(book: Book)` - удаление книги из библиотеки и индекса
	- `book`: удаляемая книга
- `find_by_isbn(isbn: str) -> Book | None` - поиск книги по ISBN
	- `isbn`: ISBN книги
- `find_by_author(author: str) -> BookCollection` - поиск книг по автору
	- `author`: автор
- `find_by_year(year: int) -> BookCollection` - поиск книг по году
	- `year`: год
- `find_by_genre(genre: str) -> BookCollection` - поиск книг по жанру
	- `genre`: жанр
- `__repr__() -> str` — строковое представление библиотеки

### Симуляция
Функции:
- `generate_random_book() -> Book` - генерация случайной книги
- `add_random_book(library: Library)` - добавление случайной книги в библиотеку
	- `library`: библиотека
- `remove_random_book(library: Library)` - удаление случайной книги из библиотеки
	- `library`: библиотека
- `search_by_author(library: Library, author: str | None = None) -> list[Book]` - поиск книг по автору
	- `library`: библиотека
	- `author`: автор (если `None`, берётся случайный из индекса)
- `search_by_year(library: Library, year: int | None = None) -> list[Book]` - поиск книг по году
	- `library`: библиотека
	- `year`: год (если `None`, берётся случайный из индекса)
- `search_by_genre(library: Library, genre: str | None = None) -> list[Book]` - поиск книг по жанру
	- `library`: библиотека
	- `genre`: жанр (если `None`, берётся случайный из коллекции)
- `update_index(library: Library)` - перестроение индекса библиотеки
	- `library`: библиотека
- `get_nonexistent_book(library: Library)` - проверка поиска по несуществующему ISBN
	- `library`: библиотека
- `run_simulation(steps: int = 20, seed: int | None = None)` - запуск симуляции на заданное число шагов с сидом
	- `steps`: количество шагов симуляции
	- `seed`: сид генератора случайных событий (если `None`, сид не фиксируется)

### CLI
- `src.main` - запуск симуляции из командной строки через аргументы `--steps` и `--seed`
- `main(argv: list[str] | None = None) -> int`
	- `argv`: список аргументов CLI (если `None`, берётся из командной строки)

## Запуск программы
Запуск симуляции осуществляется при помощи команды в терминале
```bash
python -m src.main
```

Можно задать количество шагов и сид генератора,
```bash
python -m src.main --steps 20 --seed 123
```
где `--steps` количество шагов, а `--seed` сид генератора случайных событий
