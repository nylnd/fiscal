from decimal import Decimal

from brass.bands import SlabbedBands, SteppedBands
from brass.simple_calculation import SimpleCalculation


def test_simple_calculation_slabbed_bands_threshold_not_breached():
    taxable_amount = Decimal(100_000)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert SimpleCalculation(bands, taxable_amount).liability == Decimal("0")


def test_simple_calculation_slabbed_bands_threshold_breached():
    taxable_amount = Decimal(150_000)
    bands = SlabbedBands(values=((100_000, 0), (200_000, 1)))

    assert SimpleCalculation(bands, taxable_amount).liability == Decimal("1500")


def test_simple_calculation_stepped_bands_threshold_not_breached():
    taxable_amount = Decimal(100_000)
    bands = SteppedBands(values=((100_000, 0), (200_000, 1)))

    assert SimpleCalculation(bands, taxable_amount).liability == Decimal("0")


def test_simple_calculation_stepped_bands_threshold_breached():
    taxable_amount = Decimal(150_000)
    bands = SteppedBands(values=((100_000, 0), (200_000, 1)))

    assert SimpleCalculation(bands, taxable_amount).liability == Decimal("500")
