def format_duration(seconds: int) -> str:
    if not seconds: return "now"
    origin: int = seconds
    dic: dict[str:int] = {
        'year': 60 * 60 * 24 * 365,
        'day': 60 * 60 * 24,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    spent: dict[any] = {}
    ans: str = ""
    for x in ['year', 'day', 'hour', 'minute', 'second']:
        spent[x] = seconds // dic[x]
        ans += "{}{} {}{}".format('' if seconds == origin else ' and ' if seconds % dic[x] == 0 else ', ', spent[x], x,
                                  's' if spent[x] > 1 else '') if spent[x] > 0 else ''
        seconds %= dic[x]
    return ans
