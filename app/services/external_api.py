import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"
SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
HEADERS = {
    "User-Agent": "InventoryManagement/1.0 (learning project)"
}

def get_product_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url, headers=HEADERS)
    if response .status_code != 200:
        return None
    
    data = response.json()

    if data.get("status") != 1:
        return None
    
    product = data.get("product", {})
    
    result = {
                "barcode": data.get("code"),
                "product_name": product.get("product_name"),
                "brands": product.get("brands"),
                "ingredient_text": product.get("ingredients_text"),
                "category": product.get("categories")

            }
    
   

    return result
        

def search_product_by_name(name, limit=5):
    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "page_size": limit
    }
    response = requests.get(SEARCH_URL, headers=HEADERS, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    products = data.get("products", [])

    results = []
    for product in products:
        results.append({
            "barcode": product.get("code"),
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "ingredients_text": product.get("ingredients_text"),
            "category": product.get("categories")
        })

    return results



        

