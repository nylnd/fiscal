from .abstract_calculation import AbstractCalculation


class Calculation(AbstractCalculation):
    def __init__(self, bands, taxable_amount):
        self._bands = bands
        self._taxable_amount = taxable_amount

    @property
    def taxable_amount(self):
        return self._taxable_amount

    @property
    def liability(self):
        return sum(self.taxed_bands)
