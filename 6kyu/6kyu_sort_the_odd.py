def sort_array(source_array: list[int]) -> list[int]:
    odds: list[int] = sorted((odd for odd in source_array if odd % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]
