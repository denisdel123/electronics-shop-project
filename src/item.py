import csv
import json

from pathlib import Path


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

    def __repr__(self):
        return f"Item({self.__name}, {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def names(self):
        return self.__name

    @names.setter
    def names(self, name: str):
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

    @classmethod
    def instantiate_from_csv(cls, way_csv):
        cls.all = []
        with open(way_csv, 'r', encoding='utf8') as csvfile:
            reader1 = csv.reader(csvfile)

            for row in reader1:
                cls.all.append(row)
            cls.all.pop(0)

        return reader1

    @staticmethod
    def string_to_number(count):
        return int(count)
