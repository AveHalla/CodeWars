from collections import Counter


def find_uniq(arr: list[int | float]) -> int | float:
    return sum(x for x, y in Counter(arr).items() if y == 1)
