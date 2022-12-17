from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Any


class AbstractCalculation(ABC):
    def __gt__(self, other):
        return self.liability > other.liability

    def __lt__(self, other):
        return self.liability < other.liability

    @property
    @abstractmethod
    def taxable_amount(self):
        return NotImplementedError

    @property
    @abstractmethod
    def liability(self):
        return NotImplementedError

    @property
    def bands(self):
        return self._bands

    @property
    def allocated_bands(self):
        return self.bands.allocate(self.taxable_amount)

    @property
    def taxed_bands(self) -> tuple[Decimal | Any, ...]:
        return tuple(
            (threshold * percentage / Decimal("100"))
            for threshold, percentage in self.allocated_bands
        )
