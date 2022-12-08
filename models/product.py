from useful.helper import format_float_str_currency


class Product:
    count: int = 1

    def __init__(self, name: str, price: float, ) -> None:
        self.__code: int = Product.count
        self.__name = name
        self.__price = price
        Product.count += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self:object) -> str:
        return self.__name

    @property
    def price(self: object) -> int:
        return self.__price

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nName: {self.name} \nPrice: {format_float_str_currency(self.price)}'

