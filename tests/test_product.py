import unittest
from src.product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Запускается перед каждым тестом."""
        self.product = Product("Laptop", "A high-performance laptop", 1200.99, 5)

    def test_initialization(self):
        """Проверка правильной инициализации атрибутов."""
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.description, "A high-performance laptop")
        self.assertEqual(self.product.price, 1200.99)
        self.assertEqual(self.product.quantity, 5)

    def test_name(self):
        """Проверка изменения имени продукта."""
        self.product.name = "Gaming Laptop"
        self.assertEqual(self.product.name, "Gaming Laptop")

    def test_description(self):
        """Проверка изменения описания продукта."""
        self.product.description = "A powerful gaming laptop."
        self.assertEqual(self.product.description, "A powerful gaming laptop.")

    def test_price(self):
        """Проверка изменения цены продукта."""
        self.product.price = 1300.75
        self.assertEqual(self.product.price, 1300.75)

    def test_quantity(self):
        """Проверка изменения количества продукта."""
        self.product.quantity = 10
        self.assertEqual(self.product.quantity, 10)
