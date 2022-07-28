from functools import reduce


def persistence(num: int) -> int:
    counter: int = 0
    while len(str(num)) != 1:
        num = reduce((lambda x, y: x * y), list(map(int, str(n))))
        counter += 1
    return counter
