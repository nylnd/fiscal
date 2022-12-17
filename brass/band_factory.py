from brass.allocators import slab
from brass.bands import SlabbedBands, SteppedBands


def band_factory(args):
    """
    factory method for the creation of Bands
    """

    values, allocator = args
    if allocator is slab:
        return SlabbedBands(values)
    else:
        return SteppedBands(values)
