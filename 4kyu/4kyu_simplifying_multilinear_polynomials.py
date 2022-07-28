import re


def simplify(poly: str) -> str:
    matches: list = re.findall(r'([+\-]?)(\d*)([a-z]+)', poly)
    expand: list = [[int(i[0] + (i[1] if i[1] != '' else '1')), ''.join(sorted(i[2]))] for i in matches]
    variables: list = sorted(list(set(x[1] for x in expand)), key=lambda x: (len(x), x))
    coefficient: dict = {v: sum(i[0] for i in expand if i[1] == v) for v in variables}
    return '+'.join(str(coefficient[v]) + v for v in variables if coefficient[v] != 0).replace('1', '').replace('+-',
                                                                                                                '-')
