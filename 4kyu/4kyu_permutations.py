import itertools


def permutations(string: str) -> list[str]:
    return [''.join(i) for i in set(itertools.permutations(string))]
