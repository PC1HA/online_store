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
from src.category import Category
from src.product import Smartphone, LawnGrass


if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.get_products)
    print(category_grass.get_products)
    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")

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
#### Подкласс Смартфон ```class Smartphone(Product)```
Класс, представляющий смартфон.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        __price (float): Цена продукта (приватный).
        quantity (int): Количество продукта на складе.
        efficiency (float): производительность.
        model (str): модель.
        memory (int): объем встроенной памяти.
        color (str): цвет.

#### Подкласс газонная трава ```class LawnGrass(Product)```
Класс, представляющий газонную траву.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        __price (float): Цена продукта (приватный).
        quantity (int): Количество продукта на складе.
        country (str): страна-производитель.
        germination_period (str): срок прорастания.
        color (str): цвет.

### Файл ```utils.py```

- Загрузка данных из JSON файла и создание списка категорий.

    :param file_path: Путь к JSON файлу.
    :return: Список категорий, загруженных из файла.

## Ветка тестирования кода

### Папка tests

#### Пример тестирования ```category.py``` в ```test_category.py```

```
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

```

#### Пример тестирования ```product.py``` в ```test_product.py```

```
import unittest
from typing import List
from unittest import mock  # noqa: F401

from src.product import LawnGrass, Product, Smartphone


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
        self.assertEqual(total_price, 2000.0)

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


class TestSmartphone(unittest.TestCase):

    def setUp(self) -> None:
        """Создание тестовых данных для смартфонов."""
        self.smartphone = Smartphone(
            "Смартфон 1",
            "Описание смартфона 1",
            500.0,
            20,
            efficiency=2.5,
            model="Модель 1",
            memory=64,
            color="Черный",
        )

    def test_smartphone_creation(self) -> None:
        """Тестирование создания смартфона."""
        self.assertEqual(self.smartphone.name, "Смартфон 1")
        self.assertEqual(self.smartphone.efficiency, 2.5)
        self.assertEqual(self.smartphone.memory, 64)

    def test_smartphone_price(self) -> None:
        """Тестирование изменения цены смартфона."""
        self.smartphone.price = 600.0
        self.assertEqual(self.smartphone.price, 600.0)


class TestLawnGrass(unittest.TestCase):

    def setUp(self) -> None:
        """Создание тестовых данных для газонной травы."""
        self.lawn_grass = LawnGrass(
            "Газонная трава 1",
            "Описание газонной травы 1",
            50.0,
            100,
            country="Россия",
            germination_period="10-14 дней",
            color="Зеленый",
        )

    def test_lawn_grass_creation(self) -> None:
        """Тестирование создания газонной травы."""
        self.assertEqual(self.lawn_grass.name, "Газонная трава 1")
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.assertEqual(self.lawn_grass.germination_period, "10-14 дней")

    def test_lawn_grass_price(self) -> None:
        """Тестирование изменения цены газонной травы."""
        self.lawn_grass.price = 55.0
        self.assertEqual(self.lawn_grass.price, 55.0)

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