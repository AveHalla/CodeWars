def spin_words(sentence: str) -> str:
    return " ".join(w[::-1] if len(w) >= 5 else w for w in sentence.split())
