import requests

BASE_URL = "http://127.0.0.1:5000"


def show_menu():
    print("\n--- Inventory Menu ---")
    print("1. View all products")
    print("2. View product by ID")
    print("3. Add product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Search product by barcode (online)")
    print("7. Import product by barcode")
    print("8. Exit")


def view_all_products():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())


def view_product_by_id():
    product_id = input("Enter product ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{product_id}")
    print(response.json())


def create_product():
    product_data = {
        "barcode": input("Barcode: "),
        "product_name": input("Product name: "),
        "brands": input("Brands: "),
        "ingredient_text": input("Ingredients: "),
        "category": input("Category: ")
    }
    response = requests.post(f"{BASE_URL}/inventory", json=product_data)
    print(response.json())


def edit_product():
    product_id = input("Enter product ID to update: ")
    field = input("Field to update (product_name/brands/ingredient_text/category): ")
    value = input("New value: ")
    response = requests.patch(f"{BASE_URL}/inventory/{product_id}", json={field: value})
    print(response.json())


def remove_product():
    product_id = input("Enter product ID to delete: ")
    response = requests.delete(f"{BASE_URL}/inventory/{product_id}")
    print(response.json())


def search_barcode():
    barcode = input("Enter barcode: ")
    response = requests.get(f"{BASE_URL}/search/{barcode}")
    print(response.json())


def import_barcode():
    barcode = input("Enter barcode to import: ")
    response = requests.post(f"{BASE_URL}/inventory/import/{barcode}")
    print(response.json())


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                view_all_products()
            elif choice == "2":
                view_product_by_id()
            elif choice == "3":
                create_product()
            elif choice == "4":
                edit_product()
            elif choice == "5":
                remove_product()
            elif choice == "6":
                search_barcode()
            elif choice == "7":
                import_barcode()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        except requests.exceptions.ConnectionError:
            print("Could not connect to the server. Is routes.py running?")


if __name__ == "__main__":
    main()