import math


def calculate_factorial_iterative(number: int) -> int:
    if number < 0:
        raise ValueError("number value should be 0 or greater.")
    factorial = 1
    if number >= 1:
        for i in range(1, number + 1):
            factorial = factorial * i
    return factorial


def calculate_factorial_recursive(number: int) -> int:
    if number < 0:
        raise ValueError("number value should be 0 or greater.")
    factorial = 1
    if number >= 1:
        factorial = number * calculate_factorial_recursive(number - 1)
    return factorial


def calculate_factorial_core_lib_method(number: int) -> int:
    return math.factorial(number)
