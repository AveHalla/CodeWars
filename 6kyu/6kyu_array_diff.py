def array_diff(a: list[any], b: list[any]) -> list[any]:
    return [i for i in a if i not in b]
