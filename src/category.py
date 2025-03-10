from typing import Any, List, Optional


class Category:
    """
    Класс, представляющий категорию продуктов.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        products (list): Список продуктов в категории.
        category_count (int): Общее количество созданных категорий.
        product_count (int): Общее количество продуктов в категориях.
    """

    name: str
    description: str
    products: List[Any]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Any]] = None) -> None:
        """
        Инициализация нового экземпляра класса Category.

        Параметры:
            name (str): Название категории.
            description (str): Описание категории.
            products (Optional[List[Any]]): Список продуктов в категории. По умолчанию None.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1

    def add_product(self, product: Any) -> None:
        """
        Добавление продукта в категорию.

        Параметры:
            product (Any): Продукт, который будет добавлен в категорию.
        """
        self.products.append(product)
        Category.product_count += 1
