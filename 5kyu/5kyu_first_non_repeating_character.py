def first_non_repeating_letter(string: str) -> str:
    for letter in range(len(string)):
        if list.count(list[letter]) == 1:
            return string[letter]
    return ""
