from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int, ):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        self.__name = name

    def __str__(self):
        return f"{self.__name}"

    def __repr__(self):
        return f"Phone('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_sim(self):
        return self.number_of_sim

    @number_sim.setter
    def number_sim(self, number):
        self.number_of_sim = number
        if self.number_of_sim >= 1 or self.number_of_sim <= 2:
            self.number_of_sim = number
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

