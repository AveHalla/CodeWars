def dig_pow(n: int, p: int):
    total: int = sum([int(str(n)[i]) ** (p + i) for i in range(len(str(n)))])
    return int(total / n) if total % n == 0 else -1
