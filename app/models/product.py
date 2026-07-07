class Product:
    def __init__(self, barcode, product_name, brands=None, ingredient_text=None, category=None, id=None):
        self.id = id
        self.barcode = barcode
        self.product_name = product_name
        self.brands = brands
        self.ingredient_text = ingredient_text
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "barcode": self.barcode,
            "product_name": self.product_name,
            "brands": self.brands,
            "ingredient_text": self.ingredient_text,
            "category": self.category
        }