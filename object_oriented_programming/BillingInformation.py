class BillingInformation:

    def __init__(self, phone_number: str, receivers_phone_number: str, delivery_address: str,
                 credit_card_information: str):
        self.phone_number = phone_number
        self.receivers_phone_number = receivers_phone_number
        self.delivery_address = delivery_address
        self.credit_card_information = credit_card_information
