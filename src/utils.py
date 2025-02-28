import json
from src.category import Category
from src.product import Product

def load_data_from_json(file_path):
    categories = []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for category_data in data:
            category = Category(name=category_data['name'], description=category_data['description'])

            for product_data in category_data['products']:
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity']
                )
                category.add_product(product)

            categories.append(category)

    return categories
