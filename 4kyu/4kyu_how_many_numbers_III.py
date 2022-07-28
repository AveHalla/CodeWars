import itertools


def find_all(sum_dig: int, digs: int) -> list[int]:
    combs: any = itertools.combinations_with_replacement(list(range(1, 10)), digs)
    target: list[str] = [''.join(str(x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]
