def narcissistic(value: int) -> bool:
    return value == sum(int(x) ** len(str(value)) for x in str(value))
