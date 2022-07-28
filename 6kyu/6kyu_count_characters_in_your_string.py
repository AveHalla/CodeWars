def count(string: str) -> dict[str:int]:
    return {letter: string.count(letter) for letter in string}
