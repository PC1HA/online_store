from typing import Any, Dict, List, Optional


class Product:
    """
    Класс, представляющий продукт.

    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        _price (float): Цена продукта (приватный).
        quantity (int): Количество продукта на складе.
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация нового экземпляра класса Product.

        Параметры:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены продукта."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для установки цены продукта с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if value < self.__price:
                confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): ")
                if confirm.lower() == "y":
                    self.__price = value
                    print(f"Цена успешно понижена до {self.__price}.")
                else:
                    print("Понижение цены отменено.")
            else:
                self.__price = value

    @classmethod
    def new_product(
        cls, product_data: Dict[str, Any], existing_products: Optional[List["Product"]] = None
    ) -> "Product":
        """Класс-метод для создания нового продукта."""
        name: Optional[str] = product_data.get("name")
        description: Optional[str] = product_data.get("description")
        price: Optional[float] = product_data.get("price")
        quantity: Optional[int] = product_data.get("quantity")

        if name is None or description is None or price is None or quantity is None:
            raise ValueError("Product data must contain name, description, price and quantity")

        if existing_products:
            for existing_product in existing_products:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        if price <= 0 or quantity < 0:
            raise ValueError("Цена должна быть положительной, а количество неотрицательным.")

        return cls(name, description, price, quantity)
