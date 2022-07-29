def find_nb(m: int) -> int:
    n: int = 1
    check: int = 0
    while check <= m:
        check += n ** 3
        if check == m: return n
        n += 1
    return -1
