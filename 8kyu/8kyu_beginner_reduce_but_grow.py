from functools import reduce


def grow(arr: list) -> int|float:
    return reduce(lambda x, y: x * y, arr)
