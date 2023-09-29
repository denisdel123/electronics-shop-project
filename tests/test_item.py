"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def class_test():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(class_test):
    assert class_test.calculate_total_price() == 200000


def test_apply_discount(class_test):
    assert class_test.all == [['Смартфон', 10000, 20]]
