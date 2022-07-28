def strip_comments(string: str, markers: list[str]) -> str:
    lines: list[str] = string.split('\n')
    for marker in markers:
        lines = [line.split(marker)[0].rstrip() for line in lines]
    return '\n'.join(lines)
