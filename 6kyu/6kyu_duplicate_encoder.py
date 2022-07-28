def duplicate_encode(word: str) -> str:
    return ''.join(['(' if word.lower().count(letter) == 1 else ')' for letter in word.lower()])
