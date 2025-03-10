import json
from typing import Any, Dict, List

from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загрузка данных из JSON файла и создание списка категорий.

    :param file_path: Путь к JSON файлу.
    :return: Список категорий, загруженных из файла.
    """
    categories: List[Category] = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data: List[Dict[str, Any]] = json.load(file)

            for category_data in data:
                category = Category(name=category_data['name'], description=category_data['description'])

                for product_data in category_data['products']:
                    product = Product(
                        name=product_data['name'],
                        description=product_data['description'],
                        price=product_data['price'],
                        quantity=product_data['quantity']
                    )
                    category.add_product(product)

                categories.append(category)

    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути {file_path}")
        return []

    return categories
