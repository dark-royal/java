class InvalidAmountException(BaseException):
    def __init__(self):
        super().__init__("Invalid Amount Exception.")
