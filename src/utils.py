import json
import os
from src.product import Product
from src.category import Category


def read_json(path_to_json: str) -> dict:
    full_path = os.path.abspath(path_to_json)
    with open(full_path, 'r', encoding="UTF-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    raw_data = read_json('../data/data.json')
    data = create_objects_from_json(raw_data)
    print(data)
