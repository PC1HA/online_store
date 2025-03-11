import unittest
from typing import List
from unittest import mock

from src.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.product = Product("Ноутбук", "Мощный ноутбук", 1200.00, 10)

    def test_initial_attributes(self) -> None:
        self.assertEqual(self.product.name, "Ноутбук")
        self.assertEqual(self.product.description, "Мощный ноутбук")
        self.assertEqual(self.product.price, 1200.00)
        self.assertEqual(self.product.quantity, 10)

    def test_price_setter(self) -> None:
        self.product.price = 1300.00
        self.assertEqual(self.product.price, 1300.00)

    def test_price_setter_negative_value(self) -> None:
        with mock.patch("builtins.print") as mocked_print:
            self.product.price = -500
            mocked_print.assert_called_with("Цена не должна быть нулевая или отрицательная")

    def test_price_setter_lower_value_with_confirmation(self) -> None:
        with mock.patch("builtins.input", return_value="y"):
            self.product.price = 1000.00
            self.assertEqual(self.product.price, 1000.00)

    def test_price_setter_lower_value_without_confirmation(self) -> None:
        with mock.patch("builtins.input", return_value="n"):
            self.product.price = 1000.00
            self.assertEqual(self.product.price, 1200.00)

    def test_new_product(self) -> None:
        product_data = {"name": "Смартфон", "description": "Современный смартфон", "price": 800.00, "quantity": 5}
        new_product = Product.new_product(product_data)
        self.assertEqual(new_product.name, "Смартфон")
        self.assertEqual(new_product.description, "Современный смартфон")
        self.assertEqual(new_product.price, 800.00)
        self.assertEqual(new_product.quantity, 5)

    def test_new_product_existing(self) -> None:
        existing_products: List[Product] = [self.product]
        product_data = {"name": "Ноутбук", "description": "Мощный ноутбук", "price": 1300.00, "quantity": 5}
        existing_product = Product.new_product(product_data, existing_products)
        self.assertEqual(existing_product.quantity, 15)
        self.assertEqual(existing_product.price, 1300.00)
