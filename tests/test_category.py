import unittest
from typing import List

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):

    def setUp(self) -> None:
        """Создание тестовых данных перед каждым тестом."""
        self.product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)
        self.category = Category("Категория 1", "Описание категории 1", [self.product1, self.product2])

    def test_category_creation(self) -> None:
        """Тестирование создания категории."""
        self.assertEqual(self.category.name, "Категория 1")
        self.assertEqual(self.category.description, "Описание категории 1")
        self.assertEqual(len(self.category.get_products), 2)

    def test_add_product(self) -> None:
        """Тестирование добавления продукта в категорию."""
        product3 = Product("Товар 3", "Описание товара 3", 150.0, 20)
        self.category.add_product(product3)
        self.assertEqual(len(self.category.get_products), 3)
        self.assertIn(product3, self.category.get_products)

    def test_add_invalid_product(self) -> None:
        """Тестирование добавления недопустимого продукта."""
        with self.assertRaises(TypeError):
            self.category.add_product("Некорректный продукт")   # type: ignore

    def test_str_method(self) -> None:
        """Тестирование метода __str__."""
        self.assertEqual(str(self.category), "Категория 1: 15 продуктов")  # 10 + 5

    def test_products_info(self) -> None:
        """Тестирование получения информации о продуктах."""
        expected_info = (
            f"{self.product1.name}, {self.product1.price} руб. Остаток: {self.product1.quantity} шт.\n"
            f"{self.product2.name}, {self.product2.price} руб. Остаток: {self.product2.quantity} шт."
        )
        self.assertEqual(self.category.products_info, expected_info)

    def test_iterator(self) -> None:
        """Тестирование итератора категории."""
        products: List[Product] = list(iter(self.category))
        self.assertEqual(products, [self.product1, self.product2])

    def test_average_price_with_products(self):
        """Тестирование average_price с продуктами в категории."""
        category = Category("Электроника", "Различные электронные устройства")
        category.add_product(Product("Телефон",'', 500.0, 10))
        category.add_product(Product("Ноутбук",'', 1200.0, 5))

        expected_average = (500.0 * 10 + 1200.0 * 5) / (10 + 5)
        assert category.middle_price() == expected_average

    def test_average_price_empty_category(self):
        """Тестирование average_price с пустой категорией."""
        empty_category = Category("Пустая категория", "Нет продуктов")

        assert empty_category.middle_price() == 0.0
