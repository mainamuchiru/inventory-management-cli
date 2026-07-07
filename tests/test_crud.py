import app.crud.crud as crud

crud.DATA_FILE = "test_product.json"


def test_add_product():
    product = crud.add_product({
        "barcode": "123456789",
        "product_name": "Test Product",
        "brands": "Test Brand",
        "ingredient_text": "Test Ingredients",
        "category": "Test Category"
    })
    assert product["product_name"] == "Test Product"


def test_get_all_products():
    products = crud.get_all_products()
    assert len(products) == 1


def test_get_product_by_id():
    product = crud.get_product_by_id(1)
    assert product["id"] == 1


def test_update_product():
    updated = crud.update_product(1, {"product_name": "Updated Product"})
    assert updated["product_name"] == "Updated Product"


def test_delete_product():
    deleted = crud.delete_product(1)
    assert deleted is True