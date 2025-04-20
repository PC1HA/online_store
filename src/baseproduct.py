from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> 'BaseProduct':
        """
        Минимальный шаблон для Продукта.

        :param args: Позиционные аргументы для создания продукта.
        :param kwargs: Именованные аргументы для создания продукта.
        """
        pass
