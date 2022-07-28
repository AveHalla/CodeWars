def comp(array1: list[any], array2: list[any]) -> bool:
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    return sorted([num ** 2 for num in array1]) == sorted(array2)
