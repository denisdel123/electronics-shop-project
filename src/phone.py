from src.item import Item

"""создали дочерний класс телефон который наследуется от Item """


class Phone(Item):
    """Инициализируем поле и принимаем поля от родительского класса"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int, ):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim
        self.__name = name

        """Отправляем информацию пользователю"""

    def __str__(self):
        return f"{self.__name}"

    """Отправляем информацию разработчику"""

    def __repr__(self):
        return f"Phone('{self.__name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    """установили ограничение на сложение классов"""

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    """считываем кол-во сим карт"""

    @property
    def number_of_sim(self):
        return self._number_of_sim

    """задали ограничение на кол-во сим карт"""

    @number_of_sim.setter
    def number_of_sim(self, value):
        if 0 < value < 3:
            self._number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
