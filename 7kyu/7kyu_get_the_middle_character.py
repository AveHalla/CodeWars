def get_middle(string: str) -> str:
    return string[int(len(string) / 2)] if len(string) % 2 else string[
                                                                int(len(string) / 2) - 1:int(len(string) / 2) + 1]
