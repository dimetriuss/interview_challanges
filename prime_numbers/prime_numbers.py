def find_prime_numbers_from_range(upper_number: int) -> list:
    if upper_number < 1:
        raise ValueError("Please input upper_number >= 1")

    primes = []
    for num in range(2, upper_number+1):
        for i in primes:
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


def find_prime_numbers_from_range_with_eratosthenes_sieve(upper_number: int) -> list:
    if upper_number < 1:
        raise ValueError("Please input upper_number >= 1")

    numbers_range = [x for x in range(upper_number + 1)]
    numbers_range[1] = 0
    primes = []

    filtered_number = 2
    while filtered_number <= upper_number:
        if numbers_range[filtered_number] != 0:
            primes.append(numbers_range[filtered_number])
            for number in range(filtered_number, upper_number + 1, filtered_number):
                numbers_range[number] = 0
        filtered_number += 1
    return primes


def find_prime_numbers_from_any_range(low_value: int, high_value: int) -> list:
    if low_value < 2:
        raise ValueError("Please input low_value >= 2")
    if high_value < 1 or low_value >= high_value:
        raise ValueError("Please input high_value > low_value >= 2")

    primes = []
    for num in range(2, high_value + 1):
        for i in primes:
            if num % i == 0:
                break
        else:
            primes.append(num)

    primes_in_range = [x for x in primes if x >= low_value]
    return primes_in_range
