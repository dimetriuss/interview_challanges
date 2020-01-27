def find_fibonacci_number_recursive(number_index: int) -> int:
    if number_index < 0:
        raise ValueError("Please input number_index >= 0")
    if number_index <= 1:
        return 1
    fib_number = find_fibonacci_number_recursive(number_index - 2) + find_fibonacci_number_recursive(number_index - 1)
    return fib_number


def find_fibonacci_number_iterative(number_index: int) -> int:
    if number_index < 0:
        raise ValueError("Please input number_index >= 0")
    if number_index <= 1:
        return 1

    fib_number = 0
    previous_number1 = previous_number2 = 1

    for i in range(2, number_index + 1):
        fib_number = previous_number1 + previous_number2
        previous_number2 = previous_number1
        previous_number1 = fib_number
    return fib_number


def find_fibonacci_number_golden_ratio(number_index: int) -> int:
    if number_index < 0:
        raise ValueError("Please input number_index >= 0")
    if number_index <= 1:
        return 1
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** (number_index + 1) + 1) / 5 ** 0.5)


def find_fibonacci_numbers_in_values_range(low: int, high: int) -> list:
    if low < 0:
        raise ValueError("Please input low >= 0")
    if high < 1 or low == high:
        raise ValueError("Please input high > low >= 0")

    fib_numbers = []
    previous_number1 = 0
    previous_number2 = 1
    if previous_number1 >= low:
        fib_numbers.append(previous_number1)
    if previous_number2 >= low:
        fib_numbers.append(previous_number2)

    while True:
        current_number = previous_number1 + previous_number2
        if current_number > high:
            break
        if current_number >= low:
            fib_numbers.append(current_number)
        previous_number1, previous_number2 = previous_number2, current_number

    return fib_numbers
