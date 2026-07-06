import requests


URL = f"https://world.openfoodfacts.net/api/v3.6/product/"


products = []

class openFoodsapi:
    def __init__(self,url):
        self.url = url
    
    def get_product(self,barcode):
        
        url = f"{self.url}/{barcode}"
        print(url)
        response = requests.get(url)
        products.append(response)
        print(response.json())
        print(len(products))

apifood = openFoodsapi(URL).get_product(3274080005003)