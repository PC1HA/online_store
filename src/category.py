from typing import Any, List, Optional

from src.product import Product


class Category:
    """
    Класс, представляющий категорию продуктов.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        __products (list): Список продуктов в категории (приватный).
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество продуктов в категориях.
    """

    name: str
    description: str
    __products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Any]] = None) -> None:
        """
        Инициализация нового экземпляра класса Category.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (Optional[List[Product]]): Список продуктов в категории. По умолчанию None.
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию.

        Параметры:
            product (Product): Продукт, который будет добавлен в категорию.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_info(self) -> str:
        """
        Получение списка продуктов в категории в формате строки.

        Возвращает:
            str: Информация о продуктах в категории.
        """
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        )

    def get_products(self) -> List["Product"]:
        """Возвращает список продуктов в категории."""
        return self.__products
