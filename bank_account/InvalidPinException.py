class InvalidPinException(Exception):
    def __init__(self):
        super().__init__("Invalid pin.")


