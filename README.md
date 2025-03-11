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

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products_info)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products_info)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

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

```

#### Пример тестирования ```product.py``` в ```test_product.py```

```
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
            self.assertEqual(len(categories[0].get_products()), 2)
            self.assertEqual(categories[0].get_products()[0].name, "Smartphone")
            self.assertEqual(categories[0].get_products()[1].name, "Laptop")

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