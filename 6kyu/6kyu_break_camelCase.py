def break_camel_case(sentence: str) -> str:
    return ''.join(' ' + letter if letter.isupper() else letter for letter in sentence)
