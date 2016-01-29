

def round_down_hundreds(x):
    """Rounding down to hundreds

    @param number x:    number to be rounded
    """
    import math
    return int(math.floor(x / 100.0)) * 100

