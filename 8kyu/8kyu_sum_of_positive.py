def positive_sum(arr: list[int | float]) -> int | float:
    return sum(filter(lambda x: x > 0, arr))
