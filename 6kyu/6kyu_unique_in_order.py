from itertools import groupby


def unique_in_order(iterable: any) -> any:
    return [x for x, _ in groupby(iterable)]
