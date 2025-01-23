BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """"Класс описывает объект Книга"""
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'

# TODO написать класс Library
class Library:
    """"Класс описывает Библиотеку, состоящую из списка книг"""

    def __init__(self, books: list[Book] = None):
        """"
        Инициализируем экземпляр класса Library

        :param books: books list
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """"
        Возвращает иденетификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """"
        Возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса

        :param book_id: the book's id
        """
        for index, value in enumerate(self.books):
            if value.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
