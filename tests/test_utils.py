import json
import unittest
from typing import List
from unittest.mock import mock_open, patch

from src.category import Category
from src.utils import load_data_from_json


class TestLoadDataFromJson(unittest.TestCase):

    def test_load_data_success(self) -> None:
        mock_json_data = [
            {
                "name": "Electronics",
                "description": "Devices and gadgets",
                "products": [
                    {
                        "name": "Smartphone",
                        "description": "A high-quality smartphone.",
                        "price": 699.99,
                        "quantity": 50
                    },
                    {
                        "name": "Laptop",
                        "description": "A portable computer.",
                        "price": 999.99,
                        "quantity": 30
                    }
                ]
            }
        ]

        with patch("builtins.open", mock_open(read_data=json.dumps(mock_json_data))) as mock_file:
            categories: List[Category] = load_data_from_json("dummy_path.json")

            mock_file.assert_called_once_with("dummy_path.json", 'r', encoding='utf-8')

            self.assertEqual(len(categories), 1)
            self.assertIsInstance(categories[0], Category)
            self.assertEqual(categories[0].name, "Electronics")
            self.assertEqual(len(categories[0].products), 2)
            self.assertEqual(categories[0].products[0].name, "Smartphone")
            self.assertEqual(categories[0].products[1].name, "Laptop")

    def test_load_data_file_not_found(self) -> None:
        with patch("builtins.open", side_effect=FileNotFoundError):
            categories: List[Category] = load_data_from_json("invalid_path.json")
            self.assertEqual(categories, [])
