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

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

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
        products (list): Список продуктов в категории.
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество продуктов в категориях.

   - Инициализация нового экземпляра класса Category.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (Optional[List[Any]]): Список продуктов в категории. По умолчанию None.

### Файл ```product.py```

- Класс, представляющий продукт.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        price (float): Цена продукта.
        quantity (int): Количество продукта на складе.

- Инициализация нового экземпляра класса Product.

        Параметры:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта на складе.

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

    def setUp(self):
        """Запускается перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0
        self.category = Category("Electronics", "Devices and gadgets")
        self.product1 = Product("Laptop", "A high-performance laptop", 1200.99, 10)
        self.product2 = Product("Smartphone", "A latest model smartphone", 799.99, 25)

    def test_category_initialization(self):
        """Проверка правильной инициализации атрибутов категории."""
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "Devices and gadgets")
        self.assertEqual(self.category.products, [])
        self.assertEqual(Category.category_count, 1)

    def test_add_product(self):
        """Проверка добавления продукта в категорию."""
        self.category.add_product(self.product1)
        self.assertEqual(len(self.category.products), 1)
        self.assertEqual(self.category.products[0].name, "Laptop")
        self.assertEqual(Category.product_count, 1)

        self.category.add_product(self.product2)
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(self.category.products[1].name, "Smartphone")
        self.assertEqual(Category.product_count, 2)

    def test_multiple_categories(self):
        """Проверка создания нескольких категорий."""
        category2 = Category("Home Appliances", "Appliances for home")
        self.assertEqual(Category.category_count, 2)

```

#### Пример тестирования ```product.py``` в ```test_product.py```

```
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