def queue_time(customers: list[int], n: int) -> int:
    tills: list[int] = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)
