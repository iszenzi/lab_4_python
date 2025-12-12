from src.book import Book, FictionBook, NonFictionBook
from src.collections import BookCollection


def main() -> None:
    book1 = Book(
        "Война и мир", "Л.Н.Толстой", 1869, "Роман-эпопея", "978-5-389-07123-0"
    )
    book2 = FictionBook(
        "Гарри Поттер и философский камень",
        "Дж. К. Роулинг",
        1997,
        "Фентези",
        "978-0-7475-3269-9",
    )
    book3 = NonFictionBook(
        "Коротко о главном",
        "Владимир Леви",
        2010,
        "Личностный рост",
        "978-5-901226-26-1",
    )
    print(book1)
    print(book2)
    print(book3)

    collection = BookCollection()
    collection.add_book(book1)
    collection.add_book(book2)
    collection.add_book(book3)
    print(f"\nВ коллекции {len(collection)} книг")
    print(f"book1 in collection: {book1 in collection}")
    print("Список книг:")
    for book in collection:
        print("\t", book)

    slice_collection = collection[1:3]
    print(f"\nВ коллекции {len(slice_collection)} книг")
    print("Список книг:")
    for book in slice_collection:
        print("\t", book)


if __name__ == "__main__":
    main()
