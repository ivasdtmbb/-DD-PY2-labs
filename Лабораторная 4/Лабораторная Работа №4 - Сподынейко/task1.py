class Hobby:
    """Базовый класс хобби"""

    def __init__(self, season: str, equipment: dict):
        self.__season = season
        self.__equipment = equipment

    @property
    def season(self) -> str:
        """Возвращает время года, когда занимаюсь хобби"""
        return self.__season

    @property
    def equipment(self) -> dict:
        """Возвращает снаряжение для хобби."""
        return self.__equipment

    def __str__(self):
        return f"Хобби: Сезон: {self.season}. Снаряжение: {self.equipment}"

    def __repr__(self):
        return f"{self.__class__.__name__}season={self.season!r}, equipment={self.equipment!r})"

    def get_hobby_description(self) -> str:
        """
        Возвращает описание хобби

        :return: string, описание
        """
        return f"Этим хобби я занимаюсь, когда на улице {self.season}."

    def check_equipment(self, item: str) -> bool:
        """
        Проверка, есть ли снаряжение

        :param item: Название
        :return: True, если снаряга есть, иначе False
        """
        return item in self.equipment

#-----------------------------------------------------------------------------------------------------------#
class Kayaking(Hobby):
    """Класс для хобби каякинг"""

    __name = "Каякинг"

    def __init__(self, season: str, equipment: dict, water_type: str = "неизвестно"):
        """"
        :param __water_type: Тип водоёма
        """
        super().__init__(season, equipment)
        self.__water_type = water_type

    @property
    def name(self) -> str:
        """Название хобби"""
        return self.__name

    @property
    def water_type(self) -> str:
        """Возвращает тип водоёма"""
        return self.__water_type

    def __str__(self):
        return f"Каякинг: {self.name}. Сезон: {self.season}. Водоём: {self.water_type}. Снаряжение: {self.equipment}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, season={self.season!r}, equipment={self.equipment!r}, water_type={self.water_type!r})"

    def get_hobby_description(self) -> str:
        """
        Возвращает описание хобби
        Перегруженный метод, так как нужно указать дополнительную
        информацию о типе водоёма.

        :return: string, описание
        """
        return f"Этой годнотой я занимаюсь на {self.water_type}, когда на улице {self.season}."

#-----------------------------------------------------------------------------------------------------------#
class MountainBiking(Hobby):
    """Класс для хобби горный велосипед"""

    __name = "Горный велосипед"

    def __init__(self, name: str, season: str, equipment: dict, level: str = "турбо-пушка"):
        """
        :param level: Уровень катания
        """
        super().__init__(season, equipment)
        self.__level = level

    @property
    def name(self) -> str:
        """Название хобби"""
        return self.__name

    @property
    def level(self) -> str:
        """Возвращает уровень сложности маршрута"""
        return self.__level

    def __str__(self):
        return f"Горный велосипед: {self.name}. Сезон: {self.season}. Уровень: {self.level}. Снаряжение: {self.equipment}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, season={self.season!r}, equipment={self.equipment!r}, level={self.level!r})"

    def get_hobby_description(self) -> str:
        """
        Возвращает описание хобби.
        Перегруженный метод так как необходимо указать сложность маршрута

        :return: string, описание
        """
        return f"Этой годнотой я занимаюсь, когда на улице {self.season}, мой уровень катания: {self.level}."

#-----------------------------------------------------------------------------------------------------------#



def main():

    mountain_biking = MountainBiking("Горный велосипед", "Весна",
                                     {"велосипед": 1, "шлем": 1, "перчатки": 1})

    hobby = Hobby( "Лето", {"каяк": 1, "весло": 2, "спасательный жилет": 1})
    kayaking = Kayaking(
        hobby.season,
        hobby.equipment,
        "озеро"
    )

    print("Проверка __str__:")
    print(hobby)
    print(kayaking)
    print(mountain_biking)

    print("------------------------------------------------------------")

    print("Проверка __repr__:")
    print(repr(kayaking))
    print(repr(mountain_biking))

    print("------------------------------------------------------------")

    print("Атрибуты:")
    print(f"Название хобби: {kayaking.name}")
    print(f"Сезон: {kayaking.season}")
    print(f"Снаряжение: {kayaking.equipment}")
    print(f"Уровень катания на байке: {mountain_biking.level}")
    print("------------------------------------------------------------")

    print("Методы:")
    print(hobby.get_hobby_description())
    print(kayaking.get_hobby_description())
    print(mountain_biking.get_hobby_description())
    print("------------------------------------------------------------")

    print("Проверка снаряги:")
    print(f"Каяк: {kayaking.check_equipment('каяк')}")
    print(f"Шлем:  {mountain_biking.check_equipment('шлем')}")
    print("------------------------------------------------------------")

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
