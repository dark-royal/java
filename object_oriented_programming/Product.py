import ProductCategory


class Product:
    def __init__(self, product_id: str, product_name: str, price: str, product_description: str,
                 product_category: ProductCategory):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_description = product_description
        self.product_category = product_category
