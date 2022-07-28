def alphabet_position(text: str) -> str:
    return " ".join(str(ord(x) - 96) for x in text.lower() if x.isalpha())
