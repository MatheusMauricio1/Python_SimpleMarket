from typing import List, Dict
from time import sleep
from models.product import Product
from useful.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []  # Since we are using dictionaries we may pass also a value for the key


def main() -> None:
    menu()


def menu() -> None:
    print('=======================================')
    print('============== Welcome! ================')
    print('============== Mark Eet ================')
    print('========================================')

    print('Please, select one of the following options:')
    print('1. Register a product')
    print('2. List products')
    print('3. Buy products')
    print('4. Show cart')
    print('5. Finish order')
    print('6. Exit')
    option: int = int(input('Option: '))
    if option == 1:
        register_product()
    elif option == 2:
        list_product()
    elif option == 3:
        buy_products()
    elif option == 4:
        show_cart()
    elif option == 5:
        finish_order()
    elif option == 6:
        print('Goodbye! See you soon!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()


def register_product() -> None:
    print('Product Registration')
    print('====================')
    name: str = input('Please, inform the name of the product: ')
    price: float = float(input('Please, inform the price of the product: '))

    product: Product = Product(name, price)

    products.append(product)

    print('The product has successfully been registered')
    sleep(2)
    menu()


def list_product() -> None:
    if len(products) > 0:
        print('Product Listing')
        print('===============')
        for product in products:
            print(product)
            print('===============')
            sleep(2)
    else:
        print('There still no registered products yet!')
    sleep(2)
    menu()


def buy_products() -> None:
    if len(products) > 0:
        print('Please, inform the code of the product that you wish to add to the cart: ')
        print('=========================================================================')
        print('================ Available Products =================')
        for p in products:
            print(p)
            print("=====================================================================")
            sleep(1)
        code: int = int(input('Code: '))

        product: Product = select_product_by_code(code)

        if product:
            if len(cart) > 0:
                its_in_the_cart: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print('The product quantity in your cart has been updated. ')
                        its_in_the_cart: bool = True
                        sleep(2)
                        menu()
                if not its_in_the_cart:
                    prod: Dict = {product: 1}
                    cart.append(prod)
                    print('The product has been added to the cart.')
            else:
                item = {product: 1}
                cart.append(item)
                print('The product has been added to the cart.')
                sleep(2)
                menu()

        else:
            print(f'The code {code} is invalid! ')
            sleep(2)
            menu()
    else:
        print('There still no registered products yet!')
    sleep(2)
    menu()


def show_cart() -> None:
    if len(products) > 0:
        print('Products in the cart: ')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('=====================')
                sleep(1)
    else:
        print('There are no products in the cart yet!')
        sleep(2)
        menu()


def finish_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Cart Products: ')
        for i in cart:
            for data in i.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
                print('===============')
                sleep(1)
        print(f'The total price is: {format_float_str_currency(total_value)}')
        print('Come back soon!')
        cart.clear()
        sleep(5)

    else:
        print('There is still no products in your cart yet!')
    sleep(2)
    menu()


def select_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()

