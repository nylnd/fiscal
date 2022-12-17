import abc
from decimal import Decimal
from functools import partial
from typing import Callable, Tuple

from .allocators import slab, step


class AbstractBands(abc.ABC):
    def __init__(
        self,
        values: Tuple[Tuple, ...],
    ) -> None:
        self._values = tuple(
            (Decimal(threshold), Decimal(percentage))
            for threshold, percentage in values
        )

    @property
    def _allocator(self):
        return NotImplementedError

    @property
    def allocate(self) -> Callable:
        return partial(self._allocator, bands=self._values)

    @property
    def values(self) -> tuple[tuple[Decimal, Decimal], ...]:
        """
        comprised of a tuple of tuples of Decimals: in each tuple there is a threshold and a percentage
        """
        return self._values


class SlabbedBands(AbstractBands):
    @property
    def _allocator(self):
        return slab


class SteppedBands(AbstractBands):
    @property
    def _allocator(self):
        return step
