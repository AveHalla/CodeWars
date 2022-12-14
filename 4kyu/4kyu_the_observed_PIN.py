import itertools


def get_pins(observed: str) -> list[str]:
    combinations: dict[str:list[str]] = {
        "0": ["8"],
        "1": ["2", "4"],
        "2": ["1", "3", "5"],
        "3": ["2", "6"],
        "4": ["1", "5", "7"],
        "5": ["2", "4", "6", "8"],
        "6": ["3", "5", "9"],
        "7": ["4", "8"],
        "8": ["5", "7", "9", "0"],
        "9": ["6", "8"]
    }
    pin: list[str] = [[digit] + combinations[digit] for digit in observed]
    return [''.join(i) for i in list(itertools.product(*pin))]
