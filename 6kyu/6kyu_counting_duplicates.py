def duplicate_count(text: str) -> int:
    return len(
        list(filter(lambda x: x > 1, list({letter: text.lower().count(letter) for letter in text.lower()}.values()))))
