import os
import json
from app.services.external_api import (
    get_product_barcode,
    search_product_by_name,
)
from app.models.product import Product

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "product.json"
)


def _load_products():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def _save_products(products):
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=2)


def get_all_products():
    return _load_products()


def get_product_by_id(product_id):
    products = _load_products()
    for product in products:
        if product.get("id") == product_id:
            return product
    return None


def search_products_by_name(name):
    """Search locally stored products by name (case-insensitive, partial match)."""
    products = _load_products()
    name = name.lower()
    return [
        product for product in products
        if name in (product.get("product_name") or "").lower()
    ]


def add_product(product_data):
    products = _load_products()
    new_id = max((p.get("id", 0) for p in products), default=0) + 1

    product = Product(
        barcode=product_data.get("barcode"),
        product_name=product_data.get("product_name"),
        brands=product_data.get("brands"),
        ingredient_text=product_data.get("ingredient_text"),
        category=product_data.get("category"),
        id=new_id
    )

    product_dict = product.to_dict()
    products.append(product_dict)
    _save_products(products)
    return product_dict


def update_product(product_id, updated_data):
    products = _load_products()
    for product in products:
        if product.get("id") == product_id:
            product.update(updated_data)
            _save_products(products)
            return product
    return None


def delete_product(product_id):
    products = _load_products()
    for product in products:
        if product.get("id") == product_id:
            products.remove(product)
            _save_products(products)
            return True
    return False


def import_product(barcode):
    product = get_product_barcode(barcode)
    if product is None:
        return None
    return add_product(product)


def import_product_by_name(name):
    
    results = search_product_by_name(name)
    if not results:
        return None

    first_result = results[0]
    normalized = {
        "barcode": first_result.get("barcode"),
        "product_name": first_result.get("product_name"),
        "brands": first_result.get("brands"),
        "ingredient_text": first_result.get("ingredients_text"),
        "category": first_result.get("category"),
    }
    return add_product(normalized)