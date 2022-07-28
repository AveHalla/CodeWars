def number(bus_stops: list[any]) -> int:
    return sum([stop[0] - stop[1] for stop in bus_stops])
