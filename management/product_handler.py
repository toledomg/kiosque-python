from statistics import mode
from menu import products


def get_product_by_id(id: int):

    if not type(id) == int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(product_type: str):

    if not type(product_type) == str:
        raise TypeError("product type must be a str")

    product_list = []

    for product in products:
        if product['type'] == product_type:
            product_list.append(product)
    print(product_list)
    return product_list


def product_new_id(products):
    last_id = 0
    new_id = 0
    if len(products) == 0:
        new_id += 1
    else:
        for id in products:
            if id['_id'] > last_id:
                new_id = id['_id'] + 1
                last_id = id['_id']

    return new_id


def add_product(products, **kwargs_menu):
    new_id = product_new_id(products)
    new_product = {'_id': new_id, **kwargs_menu}
    products.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)
    average_price = 0
    most_common_type = []

    for product in products:
        average_price += product['price']
        most_common_type.append(product['type'])

    most_common_type_results = mode(most_common_type)
    average_price_results = round(average_price/product_count, 2)

    return f"Products Count: {product_count} - Average Price: ${average_price_results} - Most Common Type: {most_common_type_results}"


# "Products Count: <contagem_de_produtos> - Average Price: $<preco_medio> - Most Common Type: <tipo_mais_comum>"
