def is_triangle(a: int | float, b: int | float, c: int | float) -> bool:
    return True if sum(sorted([a, b, c])[:2]) - max(sorted([a, b, c])) > 0 else False
