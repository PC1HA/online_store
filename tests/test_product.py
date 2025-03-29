import unittest
from typing import List
from unittest import mock   # noqa: F401

from src.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)

    def test_initialization(self) -> None:
        self.assertEqual(self.product1.name, "Товар 1")
        self.assertEqual(self.product1.description, "Описание товара 1")
        self.assertEqual(self.product1.price, 100.0)
        self.assertEqual(self.product1.quantity, 10)

    def test_str_method(self) -> None:
        self.assertEqual(str(self.product1), "Товар 1, 100.0 руб. Остаток: 10 шт.")

    def test_addition(self) -> None:
        total_price = self.product1 + self.product2
        self.assertEqual(total_price, 300.0)

    def test_price_setter_valid(self) -> None:
        self.product1.price = 150.0
        self.assertEqual(self.product1.price, 150.0)

    def test_price_setter_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.product1.price = -50.0

    def test_price_setter_lower(self) -> None:
        with unittest.mock.patch("builtins.input", side_effect=["y"]):
            self.product1.price = 50.0
            self.assertEqual(self.product1.price, 50.0)

    def test_new_product_creation(self) -> None:
        product_data = {"name": "Товар 3", "description": "Описание товара 3", "price": 300.0, "quantity": 20}
        new_product = Product.new_product(product_data)
        self.assertEqual(new_product.name, "Товар 3")
        self.assertEqual(new_product.price, 300.0)
        self.assertEqual(new_product.quantity, 20)

    def test_new_product_existing(self) -> None:
        existing_products: List[Product] = [self.product1]
        product_data = {"name": "Товар 1", "description": "Описание товара 1", "price": 120.0, "quantity": 5}
        updated_product = Product.new_product(product_data, existing_products)
        self.assertEqual(updated_product.quantity, 15)
        self.assertEqual(updated_product.price, 120.0)

    def test_new_product_invalid_data(self) -> None:
        product_data = {"name": "Товар 4", "description": "Описание товара 4", "price": -100.0, "quantity": 10}
        with self.assertRaises(ValueError):
            Product.new_product(product_data)
