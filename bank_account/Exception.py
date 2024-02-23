class InvalidAmountException(Exception):
    """Exception raised for invalid deposit/withdrawal amounts."""

    def _init_(self, message="Invalid amount. Amount must be positive."):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsException(Exception):
    """Exception raised for insufficient funds during a withdrawal."""

    def _init_(self, message="Insufficient funds."):
        self.message = message
        super().__init__(self.message)


class InvalidPinException(Exception):
    """Exception raised for invalid pin"""

    def _init_(self, message="Invalid pin. Incorrect PIN"):
        self.message = message
        super().__init__(self.message)


class AccountNotFoundException(Exception):
    """Exception raised for account not found"""

    def _init_(self, message="Account not found."):
        self.message = message
        super().__init__(self.message)
