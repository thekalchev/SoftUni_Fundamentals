class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [item for item in Catalogue.products if item.startswith(first_letter)]

    def __repr__(self):
        sorted_products = sorted(Catalogue.products)
        items = "\n".join(sorted_products)
        return f"Items in the {self.name} catalogue:\n{items}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
