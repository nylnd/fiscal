from decimal import Decimal

from .abstract_liability import AbstractLiability


class Liability(AbstractLiability):
    def __init__(self, bands, taxable_amount):
        self._bands = bands
        self._taxable_amount = taxable_amount

    @property
    def taxable_amount(self):
        return self._taxable_amount

    @property
    def total(self):
        return sum((liab for _, _, liab in self.breakdown))

    @property
    def _minimum(self):
        return Decimal("0")
