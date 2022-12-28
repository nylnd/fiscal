from decimal import Decimal

from brass.bands import SlabbedBands, SteppedBands
from brass.liability import Liability


def test_calculation_slabbed_bands_threshold_not_breached():
    taxable_amount = Decimal(100_000)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("0")


def test_calculation_slabbed_bands_threshold_breached():
    taxable_amount = Decimal(150_000)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("1500")


def test_calculation_stepped_bands_threshold_not_breached():
    taxable_amount = Decimal(100_000)
    bands = SteppedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("0")


def test_calculation_stepped_bands_threshold_breached():
    taxable_amount = Decimal(150_000)
    bands = SteppedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("500")
