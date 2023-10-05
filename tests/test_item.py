"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pathlib import Path

import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def class_test():
    return Item("Смартфон", 10000, 20)


@pytest.fixture()
def class_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(class_test):
    assert class_test.calculate_total_price() == 200000


def test_apply_discount(class_test):
    assert class_test.all == [['Смартфон', 10000, 20]]


def test_instantiate_from_csv(class_test):
    assert len(class_test.all) == 1


def test_string_to_number(class_test):
    assert class_test.string_to_number(10.0) <= 10
    assert class_test.string_to_number('5.5') == 5


def test_repr(class_test):
    assert repr(class_test) == 'Item(Смартфон, 10000, 20)'


def test_str(class_test):
    assert str(class_test) == 'Смартфон'


def test_add_item(class_test, class_phone):
    assert class_test + class_phone == 25
    with pytest.raises(AttributeError):
        class_test + 111


def test_add_phone(class_phone, class_test):
    assert class_phone + class_test == 25
    with pytest.raises(ValueError):
        class_phone + 111


def test_phone(class_phone):
    assert str(class_phone) == 'iPhone 14'
    assert repr(class_phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert class_phone.number_of_sim == 2
    with pytest.raises(ValueError):
        class_phone.number_of_sim = 0



