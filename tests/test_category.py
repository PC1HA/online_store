import unittest

from src.category import Category
from src.product import Product


class TestCategory(unittest.TestCase):
    def setUp(self) -> None:
        self.category = Category("Electronics", "Devices and gadgets")
        self.product1 = Product("Smartphone", "Latest model", 699.99, 10)
        self.product2 = Product("Laptop", "Gaming laptop", 1299.99, 5)

    def tearDown(self) -> None:
        Category.category_count = 0
        Category.product_count = 0

    def test_add_product(self) -> None:
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.get_products), 2)
        self.assertIn(self.product1, self.category.get_products)
        self.assertIn(self.product2, self.category.get_products)

    def test_products_info(self) -> None:
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        expected_info = f"{self.product1}\n{self.product2}"
        self.assertEqual(self.category.products_info, expected_info)

    def test_category_str(self) -> None:
        self.assertEqual(str(self.category), "Electronics: 0 продуктов")
        self.category.add_product(self.product1)
        self.assertEqual(str(self.category), "Electronics: 1 продуктов")

    def test_iterate_products(self) -> None:
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        products = [product for product in self.category]
        self.assertEqual(products, [self.product1, self.product2])

    def test_category_count(self) -> None:
        self.assertEqual(Category.category_count, 1)
        Category("Home Appliances", "Kitchen and home devices")
        self.assertEqual(Category.category_count, 2)

    def test_product_count(self) -> None:
        self.assertEqual(Category.product_count, 0)
        self.category.add_product(self.product1)
        self.category.add_product(self.product2)
        self.assertEqual(Category.product_count, 2)
