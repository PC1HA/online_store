class MixinLogger:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует экземпляр MixinLogger и выводит его представление.

        :param name: Название продукта.
        :param description: Описание продукта.
        :param price: Цена продукта.
        :param quantity: Количество продукта на складе.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        print(repr(self))

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра MixinLogger.

        :return: Строка с информацией о классе и его атрибутах.
        """
        return (f"{self.__class__.__name__}("
                f"{self.name}, "
                f"{self.description}, "
                f"{self.price}, "
                f"{self.quantity})")
