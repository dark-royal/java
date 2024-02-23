from decimal import Decimal

from commission_employee import CommissionEmployee


class SalaryEmployee(CommissionEmployee):

    def __init__(self, first_name, last_name, nin, sales, rates, base_pay):
        super().__init__(first_name, last_name, nin, sales, rates)
        self.base_pay = base_pay

    @property
    def base_pay(self):
        return self._base_pay

    @base_pay.setter
    def base_pay(self, pay):
        if pay < Decimal(0.0):
            raise ValueError("invalid")
        self._base_pay = pay

    def earning(self):
        return self.base_pay + super().earning()

    def __repr__(self):
        return f'{super().__repr__()}\n' \
               f'Salary: {self.base_pay}\n' \
               f'Salary Earning: {self.earning()}'


izu = SalaryEmployee("izu", "Miriam", 420, 10000, 15, 5000000)
print(izu)
