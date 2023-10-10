import csv
import json
import math

from pathlib import Path

key_csv = Path(__file__).parent.parent.joinpath("src").joinpath("items.csv")


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append([name, price, quantity])

        """Возвращаем разработчику информацию"""

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    """Возвращаем пользователю информацию"""

    def __str__(self):
        return f"{self.__name}"

    """возвращаем сумму сложения классов"""

    def __add__(self, other):
        return self.quantity + other.quantity

    """Считываем имя"""

    @property
    def name(self):
        return self.__name

    """задаем ограничение длины название товара"""

    @name.setter
    def name(self, name: str):
        self.__name = name
        if len(self.__name) > 10:
            self.__name = self.__name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_coast = self.price * self.quantity
        return all_coast

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

        """Возвращаем объекты класса"""

    @classmethod
    def instantiate_from_csv(cls, way_csv=key_csv):
        cls.all = []
        instances = []

        try:
            with open(way_csv, 'r', encoding='utf8') as csvfile:
                reader1 = csv.reader(csvfile)

                header = next(reader1)

                if header != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError("_Файл item.csv поврежден_")

                for row in reader1:
                    try:
                        value1 = str(row[0])
                        value2 = float(row[1])
                        value3 = int(row[2])

                    except (ValueError, IndexError):
                        continue

                    instance = cls(value1, value2, value3)
                    instances.append(instance)

        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")

        cls.all = instances

        return cls.all

    @staticmethod
    def string_to_number(count):
        count = float(count)
        count = math.floor(count)
        return count
