import unittest

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):
    """Тесты для класса Category."""

    def setUp(self) -> None:
        """Настройка тестовой среды."""
        Category.product_count = 0
        self.category = Category("Электроника", "Всякая электроника")
        self.product1 = Product("Ноутбук", "Мощный ноутбук", 1200.00, 5)
        self.product2 = Product("Смартфон", "Современный смартфон", 800.00, 10)

    def test_add_product(self) -> None:
        """Тестирование добавления продукта в категорию."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.get_products()), 2)
        self.assertIn(self.product1, self.category.get_products())
        self.assertIn(self.product2, self.category.get_products())

    def test_products_info(self) -> None:
        """Тестирование получения информации о продуктах в категории."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)

        expected_info = "Ноутбук, 1200.0 руб. Остаток: 5 шт.\n" "Смартфон, 800.0 руб. Остаток: 10 шт."
        self.assertEqual(self.category.products_info, expected_info)

    def test_initial_category_count(self) -> None:
        """Тестирование начального количества категорий."""
        initial_count = Category.category_count
        Category("Бытовая техника", "Техника для дома")
        self.assertEqual(Category.category_count, initial_count + 1)

    def test_product_count(self) -> None:
        """Тестирование общего количества продуктов в категориях."""
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(Category.product_count, 2)
