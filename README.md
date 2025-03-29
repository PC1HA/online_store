# Онлайн магазин

## Краткое описание

Данный проект представляет собой совокупностью функций для онлайн магазина


## Установка и использование

- Для использования данной библиотеки необходимо иметь установленный Python версии 3.6 и выше.
Убедитесь, что у вас установлен пакет datetime, который входит в стандартную библиотеку Python.
- Склонируйте репозиторий:

    [git clone](https://https://github.com/PC1HA/online_store.git)
- Убедитесь, что у вас установлен Python и необходимые библиотеки.
- Лучше всего будет использовать всё через файл main.py, пропишите импорты
    и данные, с которыми будете работать

## Примеры использования

### Файл main.py
Основной файл всего проекта, через который стоит работать и тестировать. 
Отвечает за основную логику проекта и связывает функциональности между собой.
Пример для конфига ```main.py```

```
import os
from pathlib import Path

from src.category import Category
from src.product import Product
from src.utils import load_data_from_json


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.get_products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    file_path = os.path.join(Path(__file__).parent, 'data/products.json')
    categories = load_data_from_json(file_path)

    for category in categories:
        print(category)

```

### Файл ```categoty.py```

   - Класс, представляющий категорию продуктов.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        __products (list): Список продуктов в категории (приватный).
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество продуктов в категориях.

   - Инициализация нового экземпляра класса Category.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (Optional[List[Any]]): Список продуктов в категории. По умолчанию None.
   - ```add_product```


        Добавление продукта в категорию.

        Параметры:
            product (Product): Продукт, который будет добавлен в категорию.

   - ``` @property products_info ```
    
    Получение списка продуктов в категории в формате строки.

    Возвращает:
        str: Информация о продуктах в категории.

   - ```get_products```
    
    Возвращает список продуктов в категории.

### Файл ```product.py```

- Класс, представляющий продукт.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        __price (float): Цена продукта (приватный).
        quantity (int): Количество продукта на складе.

- Инициализация нового экземпляра класса Product.

        Параметры:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта на складе.

- ``` @property price```

      Геттер для получения цены продукта.
- ```@price.setter price ```

    Сеттер для установки цены продукта с проверкой.

- ```@classmethod new_product```

    Класс-метод для создания нового продукта.

### Файл ```utils.py```

- Загрузка данных из JSON файла и создание списка категорий.

    :param file_path: Путь к JSON файлу.
    :return: Список категорий, загруженных из файла.

## Ветка тестирования кода

### Папка tests

#### Пример тестирования ```category.py``` в ```test_category.py```

```
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

```

#### Пример тестирования ```product.py``` в ```test_product.py```

```
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

```

#### Пример тестирования ```utils.py``` в ```test_utils.py```

```
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
                        "quantity": 50,
                    },
                    {"name": "Laptop", "description": "A portable computer.", "price": 999.99, "quantity": 30},
                ],
            }
        ]

        with patch("builtins.open", mock_open(read_data=json.dumps(mock_json_data))) as mock_file:
            categories: List[Category] = load_data_from_json("dummy_path.json")

            mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")

            self.assertEqual(len(categories), 1)
            self.assertIsInstance(categories[0], Category)
            self.assertEqual(categories[0].name, "Electronics")
            self.assertEqual(len(categories[0].get_products), 2)
            self.assertEqual(categories[0].get_products[0].name, "Smartphone")
            self.assertEqual(categories[0].get_products[1].name, "Laptop")

    def test_load_data_file_not_found(self) -> None:
        with patch("builtins.open", side_effect=FileNotFoundError):
            categories: List[Category] = load_data_from_json("invalid_path.json")
            self.assertEqual(categories, [])

```

## Лицензия

### MIT License

**Copyright (c) 2025 Попов Илья Игоревич**

*Разрешение предоставляется, бесплатно, любому, кто получает копию этого программного обеспечения и*
*связанных с ним документов (далее — "Программное обеспечение"), использовать Программное обеспечение без ограничений,*
*включая, но не ограничиваясь правами на использование, копирование, изменение, слияние, публикацию, распространение,*
*сублицензирование и/или продажу копий Программного обеспечения, а также разрешение лицам,*
*которым предоставляется Программное обеспечение, делать это, при соблюдении следующих условий:*

*Вышеуказанное уведомление о авторских правах и это разрешение должны быть включены во все копии или*
*значительные части Программного обеспечения.*

*Программное обеспечение предоставляется "как есть", без каких-либо гарантий, явных или подразумеваемых, включая,*
*но не ограничиваясь, гарантии товарной пригодности, соответствия определенной цели и ненарушения.*
*В любом случае авторы или правообладатели не несут ответственности за любые претензии, ущерб или*
*другие обязательства, будь то в действии, контракте или ином, возникающие из,*
*в связи с или в результате использования Программного обеспечения или других действий с ним.*