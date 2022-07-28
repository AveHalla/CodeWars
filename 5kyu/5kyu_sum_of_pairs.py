def sum_pairs(ints: list[int], sum_pair: int) -> list[int]:
    cache: set = set()
    for i in ints:
        if sum_pair - i in cache:
            return [sum_pair - i, i]
        cache.add(i)
