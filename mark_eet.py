from typing import List, Dict
from time import sleep
from models.product import Product
from useful.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []  # Since we are using dictionaries we may pass also a value for the key


def main() -> None:
    menu()


def menu() -> None:
    pass


def register_product() -> None:
    pass


def list_product() -> None:
    pass


def but_product() -> None:
    pass


def show_cart() -> None:
    pass


def close_order() -> None:
    pass


def take_product_by_order() -> None:
    pass


if __name__ == '__Main__':
    main()

