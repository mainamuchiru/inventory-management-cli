import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from app.services.external_api import get_product_barcode, search_product_by_name

from app.crud.crud import (
    get_all_products,
    get_product_by_id,
    add_product,
    update_product,
    delete_product,
    import_product,
    search_products_by_name,
    import_product_by_name
)

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Welcome to my e-commerce website"}), 200


@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(get_all_products()), 200


@app.route("/inventory/<int:product_id>", methods=["GET"])
def get_item(product_id):
    product = get_product_by_id(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


@app.route("/inventory", methods=["POST"])
def create_product():
    data = request.get_json()
    product = add_product(data)
    return jsonify(product), 201


@app.route("/inventory/<int:product_id>", methods=["PATCH"])
def edit_product(product_id):
    data = request.get_json()
    product = update_product(product_id, data)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


@app.route("/inventory/<int:product_id>", methods=["DELETE"])
def remove_item(product_id):
    deleted = delete_product(product_id)
    if not deleted:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted"}), 200


@app.route("/search/<barcode>", methods=["GET"])
def search_product(barcode):
    product = get_product_barcode(barcode)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200


@app.route("/search/name", methods=["GET"])
def search_by_name_online():
    """Search OpenFoodFacts (external) by name."""
    name = request.args.get("q", "")
    if not name:
        return jsonify({"error": "Missing query param 'q'"}), 400
    results = search_product_by_name(name)
    if not results:
        return jsonify({"error": "No products found"}), 404
    return jsonify(results), 200


@app.route("/inventory/import/<barcode>", methods=["POST"])
def add_product_inventory(barcode):
    product = import_product(barcode)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 201


@app.route("/inventory/search", methods=["GET"])
def search_inventory():
    """Search your local inventory (product.json) by name."""
    name = request.args.get("name", "")
    results = search_products_by_name(name)
    return jsonify(results), 200


@app.route("/inventory/import/name", methods=["POST"])
def add_product_by_name():
    """Search OpenFoodFacts by name and import the first match into inventory."""
    name = request.args.get("q", "")
    if not name:
        return jsonify({"error": "Missing query param 'q'"}), 400
    product = import_product_by_name(name)
    if product is None:
        return jsonify({"error": "No products found"}), 404
    return jsonify(product), 201


if __name__ == "__main__":
    app.run(debug=True)