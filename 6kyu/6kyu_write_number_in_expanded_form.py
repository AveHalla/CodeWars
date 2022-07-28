def expanded_form(num: int) -> str:
    digs: list[str] = [dig for dig in str(num)]
    for i in range(len(digs)):
        digs[i] += "0" * (len(digs) - i - 1)
    return ' + '.join(dig for dig in digs if int(dig) != 0)
