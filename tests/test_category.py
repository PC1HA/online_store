import unittest

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):

    def setUp(self) -> None:
        """Запускается перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0
        self.category: Category = Category("Electronics", "Devices and gadgets")
        self.product1: Product = Product("Laptop", "A high-performance laptop", 1200.99, 10)
        self.product2: Product = Product("Smartphone", "A latest model smartphone", 799.99, 25)

    def test_category_initialization(self) -> None:
        """Проверка правильной инициализации атрибутов категории."""
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Devices and gadgets")
        self.assertEqual(self.category.products, [])
        self.assertEqual(Category.category_count, 1)

    def test_add_product(self) -> None:
        """Проверка добавления продукта в категорию."""
        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(self.category.products[0].name, "Laptop")
        self.assertEqual(Category.product_count, 1)

        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(self.category.products[1].name, "Smartphone")
        self.assertEqual(Category.product_count, 2)

    def test_multiple_categories(self) -> None:
        """Проверка создания нескольких категорий."""
        category2: Category = Category("Home Appliances", "Appliances for home")
        self.assertEqual(Category.category_count, 2)
