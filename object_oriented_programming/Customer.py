import BillingInformation
import ShoppingCart


class Customer:
    def __init__(self, billing_information: list < BillingInformation > BillingInformation,
                 shopping_cart: ShoppingCart):
        self.billing_information = billing_information
        self.shopping_cart = shopping_cart
