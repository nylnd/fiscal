from decimal import Decimal
from math import inf

from fiscal.bands import SlabbedBands, SteppedBands
from fiscal.liability import Liability


def test_calculation_slabbed_bands_threshold_not_breached():
    taxable_amount = Decimal(100_000)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("0")


def test_calculation_slabbed_bands_threshold_just_breached():
    taxable_amount = Decimal(100_001)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert Liability(bands, taxable_amount).total == Decimal("1000.01")


def test_calculation_slabbed_bands_threshold_clearly_breached():
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


def test_calculation_stepped_bands_last_threshold_breached():
    taxable_amount = Decimal(350_000)
    bands = SteppedBands(values=((100_000, 0), (200_000, 1), (inf, 2)))

    assert Liability(bands, taxable_amount).total == Decimal("3000")
