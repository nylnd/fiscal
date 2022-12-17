from decimal import Decimal

from brass.allocators import slab, step
from brass.band_factory import band_factory

old_rates = band_factory(
    (
        (
            (150_000, 0),
            (100_000, 1),
            (250_000, 3),
            ("Infinity", 4),
        ),
        slab,
    )
)

modern_rates = band_factory(
    (
        ((150_000, 0), (100_000, 2), ("Infinity", 5)),
        step,
    )
)


def test_step_allocator_on_threshold():
    allocation = modern_rates.allocate(Decimal("250000"))
    assert allocation == (
        (Decimal("150000"), Decimal("0")),
        (Decimal("100000"), Decimal("2")),
        (Decimal("0"), Decimal("5")),
    )


def test_step_allocator_allocation_just_over_threshold():
    allocation = modern_rates.allocate(Decimal("250001"))
    assert allocation == (
        (Decimal("150000"), Decimal("0")),
        (Decimal("100000"), Decimal("2")),
        (Decimal("1"), Decimal("5")),
    )


def test_slab_allocator_just_under_nil_rate_threshold():
    allocation = old_rates.allocate(Decimal("100000"))
    assert allocation == (
        (Decimal("100000"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_into_first_positive_rate_band():
    allocation = old_rates.allocate(Decimal("200000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("200000"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_on_band_threshold():
    allocation = old_rates.allocate(Decimal("250000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("250000"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_penultimate_threshold():
    allocation = old_rates.allocate(Decimal("300000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("300000"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_fill_penultimate_threshold():
    allocation = old_rates.allocate(Decimal("500000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("500000"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_multiplier_method_final_threshold():
    allocation = old_rates.allocate(Decimal("500001"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("500001"), Decimal("4")),
    )
