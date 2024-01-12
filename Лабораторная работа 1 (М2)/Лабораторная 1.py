# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self, brand: str, model: str, year: int):
        """
        Класс "Автомобиль".

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def start(self) -> str:
        """
        Метод для запуска двигателя автомобиля.

        :return: Строка с информацией о том, что автомобиль запущен.

         Пример:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.start()
        """
        ...
    def drive(self, speed: int) -> str:
        """
        Метод для движения автомобиля.

        :param speed: Скорость движения автомобиля.
        :return: Строка с информацией о движении автомобиля с заданной скоростью.

         Пример:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.drive(60)
        """
        ...
    def stop(self) -> str:
        """
        Метод для остановки автомобиля.

        :return: Строка с информацией о том, что автомобиль остановлен.

        Пример:
        >>> car = Car("Toyota", "Camry", 2022)
        >>> car.stop()
        """
        ...



class diet:
    def __init__(self, calories_consumed: int, consumable_calories: int, calories_needed: int):
        """
        :param calories_consumed: Количество потребляемых калорий
        :param consumable_calories: Количество расходуемых калорий
        """
        if not all(isinstance(value, int) for value in [calories_consumed, consumable_calories, calories_needed]):
            raise TypeError("Количество всех калорий должно быть типа int")
        if any(value <= 0 for value in [calories_consumed, consumable_calories, calories_needed]):
            raise ValueError("Количество всех калорий дожно быть положительным числом")
        self.calories_consumed = calories_consumed
        self.consumable_calories = consumable_calories
        self.calories_needed = calories_needed
    def calories_for_life(self) -> int:
        """
        Функция, которая показывает сколько человеку нужно калорий в день
        :return: Количество калорий
        """
        ...
    def adding_calories (self, add_calories: int) -> None:
        """
        Потребляем калории в течение дня

        :param add_calories: Количество потребляемых калорий в течение дня
        :raise ValueError: Если количество потребляемых калорий меньше необходимых
        """
        if not isinstance(add_calories, (int)):
            raise TypeError("Добавляемое количество калорий должно быть типа int")
        if add_calories < 0:
            raise ValueError("Добавляемое количество калорий должно быть положительным числом")
        ...
    def remove_calories (self, calories_burned: int) -> int:
        """
        Потраченные калории в течение дня

        :param calories_burned: Количество потраченных калорий в течение дня
        :raise ValueError: Если количество потраченных калорий меньше, чем количество потребляемых калорий и больше, чем калорий для жизни, то возвращается ошибка
        :return: Количество реально потраченных калорий

        Примеры:
         calories = Diet(2200, 1800)
         calories.remove_calories(2000)
        """
        ...



class plant:
    def __init__(self, name: str, colour: str, height: float):
        """
        Класс "растение".

        :param name: Название растения.
        :param colour: Цвет цветков растения.
        :param height: Высота растения.
        """
        self.name = name
        self.colour = colour
        self.height = height

    def growth(self):
        """
        Метод, описывающий процесс роста растения.

        :return: Название растения, которое растет.
        """
        ...
    def blossom(self):
        """
        Метод, описывающий процесс цветения растения.

        :return: Название растения, которое цветет.
        """
        ...
    def care(self, level_of_humidity: float) -> str:
        """
        Метод для ухода за растением.

        :param level_of_humidity: Уровень влажности почвы.
        :return: Строка, описывающая рекомендации по уходу за растением.

        Пример:
        >>> rose = plant("Роза", "Красный", 40)
        >>> rose.care(0.8)
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass


