import unittest
import time
from prime_numbers import find_prime_numbers_from_range, find_prime_numbers_from_range_with_eratosthenes_sieve


class TestPrimeNumbersSearch(unittest.TestCase):

    def test_search_primes_in_the_range(self):
        start_time = time.time()
        result = find_prime_numbers_from_range(100)
        result_time = time.time() - start_time
        print("\nTiming for finding prime numbers in range (0, 100] is {} s".format(result_time))
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                           61, 67, 71, 73, 79, 83, 89, 97]
        self.assertListEqual(expected_result, result)

    def test_search_primes_in_the_range_with_eratosthenes_sieve(self):
        start_time = time.time()
        result = find_prime_numbers_from_range_with_eratosthenes_sieve(100)
        result_time = time.time() - start_time
        print("\nTiming for finding prime numbers in range (0, 100] via Eratosthenes sieve method is {} s".format(
            result_time))
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                           61, 67, 71, 73, 79, 83, 89, 97]
        self.assertListEqual(expected_result, result)

    def test_which_method_to_find_primes_is_faster_on_great_number_ranges(self):
        upper_number = 100000
        start_time1 = time.time()
        result1 = find_prime_numbers_from_range(upper_number)
        result_time_iterative = time.time() - start_time1
        start_time2 = time.time()
        result2 = find_prime_numbers_from_range_with_eratosthenes_sieve(upper_number)
        result_time_eratosthenes_sieve = time.time() - start_time2
        print("\n Timing for iterative primes search in (0; {}] is {}".format(upper_number, result_time_iterative))
        print("\n Timing for Eratosthenes sieve primes search in (0; {}] is {}".format(
            upper_number, result_time_eratosthenes_sieve))
        self.assertListEqual(result1, result2)
        self.assertLess(result_time_eratosthenes_sieve, result_time_iterative)
