"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture()
def class_item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def class_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture()
def class_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_item_calculate_total_price(class_item):
    assert class_item.calculate_total_price() == 200000


def test_item_apply_discount(class_item):
    assert class_item.all == [['Смартфон', 10000, 20]]


def test_item_instantiate_from_csv(class_item):
    assert len(class_item.all) == 1


def test_item_string_to_number(class_item):
    assert class_item.string_to_number(10.0) <= 10
    assert class_item.string_to_number('5.5') == 5


def test_item_repr(class_item):
    assert repr(class_item) == 'Item(Смартфон, 10000, 20)'


def test_item_str(class_item):
    assert str(class_item) == 'Смартфон'


def test_item_add(class_item, class_phone):
    assert class_item + class_phone == 25
    with pytest.raises(AttributeError):
        class_item + 111


def test_phone_add(class_phone, class_item):
    assert class_phone + class_item == 25
    with pytest.raises(ValueError):
        class_phone + 111


def test_phone_str(class_phone):
    assert str(class_phone) == 'iPhone 14'


def test_phone_repr(class_phone):
    assert repr(class_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phon_number_of_sim(class_phone):
    assert class_phone.number_of_sim == 2

    with pytest.raises(ValueError):
        class_phone.number_of_sim = 0


def test_keyboard_change_lang(class_keyboard):
    assert str(class_keyboard) == 'Dark Project KD87A'
    assert str(class_keyboard.language) == "EN"

    class_keyboard.change_lang()
    assert class_keyboard.language == 'RU'
    with pytest.raises(AttributeError):
        class_keyboard.language = "KZ"


def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_not():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
