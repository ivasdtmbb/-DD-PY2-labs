class Book:
    """Базовый класс Book."""

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self.__name

    @property
    def author(self) -> str:
        """Возвращает автора."""
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс PaperBook."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.__pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        """Устанавливает количество страниц."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.__pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Класс AudioBook."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.__duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self.__duration = float(value)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} ч."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

def main():
    book = Book("Понедельник начинается в субботу", "А. и Б. Стругацкие")
    paper_book = PaperBook("Понедельник начинается в субботу", "А. и Б. Стругацкие", 333)
    audio_book = AudioBook("Понедельник начинается в субботу", "А. и Б. Стругацкие", 4.4)

    print("Проверка метода __str__:")
    print(book)
    print(paper_book)
    print(audio_book)
    print("------------------------------------------------------------")

    print("Проверка метода __repr__:")
    print(repr(book))
    print(repr(paper_book))
    print(repr(audio_book))
    print("------------------------------------------------------------")

    print("Проверка свойств:")
    print(f"Название книги: {book.name}")  # 1984
    print(f"Автор книги: {book.author}")  # George Orwell
    print(f"Количество страниц бумажной книги: {paper_book.pages}")  # 328
    print(f"Продолжительность аудиокниги: {audio_book.duration} ч.")  # 11.5
    print("------------------------------------------------------------")

    try:
        paper_book.pages = -100
    except ValueError as e:
        print(f"Error при установке pages: {e}")

    print("------------------------------------------------------------")
    try:
        audio_book.duration = "kljlkjlkjl"
    except TypeError as e:
        print(f"Error при установке duration: {e}")

    print("------------------------------------------------------------")
    try:
        book.name = "Другое название"
    except AttributeError as e:
        print(f"Error при установке name: {e}")

    print("------------------------------------------------------------")
    try:
        book.author = "Другой автор"
    except AttributeError as e:
        print(f"Ошибка при изменении author: {e}")

if __name__ == "__main__":
    main()