def tribonacci(signature: list[int], n: int) -> list[int]:
    res: list[int] = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res
