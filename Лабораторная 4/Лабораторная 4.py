if __name__ == "__main__":
    class Animal:
        """Базовый класс для животных."""

        def __init__(self, species: str, age: int):
            """Инициализация животного."""
            self._species = species
            self._age = age

        def make_sound(self) -> str:
            """Издает звук."""
            pass  # В реализации этого метода будут определены звуки для каждого вида животного

        def __str__(self) -> str:
            """Возвращает строковое представление животного."""
            return f"{self._species} - Возраст: {self._age} лет"

        def __repr__(self) -> str:
            """Возвращает строковое представление животного для отладки."""
            return f"{self.__class__.__name__}(species={self._species!r}, age={self._age!r})"


    class Dog(Animal):
        """Класс для собак, унаследованный от базового класса Животные."""

        def __init__(self, species: str, age: int, breed: str, name: str):
            """Инициализация собаки."""
            super().__init__(species, age)
            self._breed = breed
            self._name = name

        def wag_tail(self) -> None:
            """Виляет хвостом."""
            pass  # В реализации этого метода будет описано движение хвостом у собаки

        def __str__(self) -> str:
            """Возвращает строковое представление собаки."""
            return super().__str__() + f", Порода: {self._breed}, Кличка: {self._name}"

        # Перегрузка метода __repr__ не требуется, так как он унаследован и адаптирован к дочернему классу.

    dog = Dog("Собака", 3, "Бульдог", "Коржик")
    print(dog)
    dog.make_sound()  # Здесь вы можете добавить реальную реализацию для метода make_sound
    dog.wag_tail()  # Здесь вы можете добавить реальную реализацию для метода wag_tail




