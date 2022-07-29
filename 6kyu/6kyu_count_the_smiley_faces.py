import re


def count_smileys(arr: list[str]) -> int:
    return len(re.findall('[:;][-~]?[)D]', str(arr)))



