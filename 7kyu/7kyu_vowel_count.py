def get_count(sentence: str) -> int:
    return sum(map(sentence.lower().count, "aeiou"))
