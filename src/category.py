from typing import Any, Iterator, List, Optional

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

    def __str__(self) -> str:
        return f"{self.name}: {sum(product.quantity for product in self.__products)} продуктов"

    def __iter__(self) -> "CategoryIterator":
        return CategoryIterator(self)

    def add_product(self, product: Product) -> None:
        """
        Добавление продукта в категорию.

        Параметры:
            product (Product): Продукт, который будет добавлен в категорию.
        """
        if not isinstance(product, Product):
            raise TypeError("Ожидается объект типа Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_info(self) -> str:
        """
        Получение списка продуктов в категории в формате строки.

        Возвращает:
            str: Информация о продуктах в категории.
        """
        return "\n".join(str(product) for product in self.__products)

    @property
    def get_products(self) -> List["Product"]:
        """Возвращает список продуктов в категории."""
        return self.__products

    def middle_price(self) -> float:
        """
                Подсчитывает среднюю цену всех товаров в категории.

                Возвращает:
                    float: Средняя цена товаров. Если товаров нет, возвращает 0.

                Исключения:
                    ZeroDivisionError: Если сумма всех цен делится на ноль.

                Примечание:
                    Если нет товаров в категории, возвращается 0 без выбрасывания исключения.
                """
        try:
            if not self.__products:
                return 0.0

            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)

            if total_quantity == 0:
                return 0.0

            average = total_price / total_quantity
            return average

        except ZeroDivisionError:
            return 0.0


class CategoryIterator(Iterator):
    def __init__(self, category: "Category"):
        """
        Инициализирует итератор для категории.

        :param category: Объект категории, по товарам которой будет производиться итерация.
        """
        self.category = category
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        """
        Возвращает сам объект итератора.

        :return: Объект CategoryIterator.
        """
        return self

    def __next__(self) -> "Product":
        """
        Возвращает следующий продукт в категории.

        :return: Следующий продукт в категории.

        :raises StopIteration: Если все продукты были перебраны.
        """
        if self.index < len(self.category.get_products):
            product = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
