class Product:
    def __init__(self,id,barcode,name):
        self.id = id
        self.barcode =  barcode
        self.name =name
        
    def add_product(self):
        products = {"id": self.id,"barcode": self.barcode, "name":self.name}