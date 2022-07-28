def is_prime(num: int) -> bool:
    if num > 1:
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True
    else:
        return False
