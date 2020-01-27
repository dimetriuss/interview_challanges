from math import sqrt


def get_squared_ints_from_range(low: int, high: int) -> list:
    if low < 0:
        raise ValueError("Please input low >= 0")
    if high <= low:
        raise ValueError("Please input high > low >= 0")

    results = []
    for i in range(low, high + 1):
        fractional_number_part = str(sqrt(i)).split('.')[1]
        if fractional_number_part == '0':
            results.append(i)
    return results
