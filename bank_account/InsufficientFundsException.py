class InsufficientFundsException(BaseException):
    def __init__(self):
        super().__init__("Insufficient funds.")
