from decimal import Decimal
from typing import Any, Callable, Tuple


def step(amount: Decimal, bands: list[Decimal]) -> tuple[tuple[Decimal, Any], ...]:
    """
    Step allocations work by allocating the amount to the amounts in bands, in order, until nothing is left.
    """

    def allocable(amount: Decimal) -> Callable[[Decimal], Decimal]:
        def allocate_to(threshold):
            nonlocal amount
            allocation = min(amount, threshold)
            amount -= allocation
            return allocation

        return allocate_to

    allocable_amount = allocable(amount)
    return tuple((allocable_amount(t), p) for t, p in bands)


def slab(amount: Decimal, bands: list[Decimal]) -> tuple[tuple[Decimal, Any], ...]:
    """
    Slab allocations work by comparing the provided amount with the cumulative threshold at a given band.
    In the band when the amount first exceeds the cumulative threshold of a band, the amount is allocated to the next band.
    """

    def allocable(amount: Decimal) -> Callable[[Decimal], Decimal]:
        def allocate_to(threshold):
            nonlocal amount
            if amount > threshold:
                return Decimal("0")
            else:
                allocation, amount = amount, Decimal("0")
                return allocation

        return allocate_to

    running_total = 0
    cumulative_thresholds = (
        running_total := running_total + threshold for threshold, _ in bands
    )
    allocable_amount = allocable(amount)
    return tuple(
        zip((allocable_amount(t) for t in cumulative_thresholds), (p for _, p in bands))
    )
