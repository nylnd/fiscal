from decimal import Decimal

from fiscal.bands import SlabbedBands, SteppedBands

slabbed_bands = SlabbedBands(
    (
        (150_000, 0),
        (100_000, 1),
        (250_000, 3),
        ("Infinity", 4),
    )
)


stepped_bands = SteppedBands(
    (
        (150_000, 0),
        (100_000, 2),
        ("Infinity", 5),
    )
)


def test_step_allocator_on_threshold():
    allocation = stepped_bands.allocate(Decimal("250000"))
    assert allocation == (
        (Decimal("150000"), Decimal("0")),
        (Decimal("100000"), Decimal("2")),
        (Decimal("0"), Decimal("5")),
    )


def test_step_allocator_allocation_just_over_top_threshold():
    allocation = stepped_bands.allocate(Decimal("250001"))
    assert allocation == (
        (Decimal("150000"), Decimal("0")),
        (Decimal("100000"), Decimal("2")),
        (Decimal("1"), Decimal("5")),
    )


def test_slab_allocator_just_under_nil_rate_threshold():
    allocation = slabbed_bands.allocate(Decimal("100000"))
    assert allocation == (
        (Decimal("100000"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_into_first_positive_rate_band():
    allocation = slabbed_bands.allocate(Decimal("200000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("200000"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_on_band_threshold():
    allocation = slabbed_bands.allocate(Decimal("250000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("250000"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_just_over_band_threshold():
    allocation = slabbed_bands.allocate(Decimal("250001"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("250001"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_penultimate_threshold():
    allocation = slabbed_bands.allocate(Decimal("300000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("300000"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_allocator_fill_penultimate_threshold():
    allocation = slabbed_bands.allocate(Decimal("500000"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("500000"), Decimal("3")),
        (Decimal("0"), Decimal("4")),
    )


def test_slab_multiplier_method_final_threshold():
    allocation = slabbed_bands.allocate(Decimal("500001"))
    assert allocation == (
        (Decimal("0"), Decimal("0")),
        (Decimal("0"), Decimal("1")),
        (Decimal("0"), Decimal("3")),
        (Decimal("500001"), Decimal("4")),
    )
