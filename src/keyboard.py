from src.item import Item

"""создал миксин класс"""


class MixinLog:
    """Инициализировал язык"""

    def __init__(self):
        self._language = "EN"

        """функция по замене языка"""

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

            """считывает поле"""

    @property
    def language(self):
        return self._language

    """Проверяем является ли значение допустимым языком"""

    @language.setter
    def language(self, value):
        if value == "EN" or value == "RU":
            self._language = value

        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")


"""класс наследующийся от Item и MixinLog"""


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)

        """отправляем информацию пользователю"""

    def __str__(self):
        return f"{self.name}"
