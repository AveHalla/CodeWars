import string


def is_pangram(s: str) -> bool:
    return not set(string.ascii_lowercase) - set(s.lower())
