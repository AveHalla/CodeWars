def increment_string(string: str) -> str:
    head: str = string.rstrip("0123456789")
    tail: str = string[len(head):]
    if tail == "": return string + "1"
    return head + str(int(tail) + 1).zfill(len(tail))
