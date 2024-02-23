from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, nin, sales, rates):
        self._first_name = first_name
        self._last_name = last_name
        self._nin = nin
        self._sales = sales
        self._rates = rates

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def nin(self):
        return self._nin

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError(f'Invalid amount{value}')
        self._sales = value

    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self, rates):
        if Decimal(0.0) < rates < Decimal(1.0):
            raise ValueError(f'invalid rate amount {rates}')
        self._rates = rates

    def earning(self):
        return self.sales * (self.rates / 100)

    def __repr__(self):
        return f'first name:{self._first_name}\nlast name: {self._last_name}\n' \
               f'Nin: {self._nin}\nEarning:{self.earning()}'


bioke = CommissionEmployee("Abbey", "Hannah", 419, 1200, 5)
#print(bioke)
