import unittest
import time
from fibonacci import find_fibonacci_number_recursive, find_fibonacci_number_iterative, \
	find_fibonacci_number_golden_ratio, find_fibonacci_numbers_in_values_range


class TestFibonacciSequenceNumber(unittest.TestCase):

	def test_recursive_fibonacci_number(self):
		start_time = time.time()
		result = find_fibonacci_number_recursive(40)
		result_time = time.time() - start_time
		print("\nTiming for finding 40th fibonacci sequence number with recursive method is {} s".format(result_time))
		expected_result = 165580141
		self.assertEqual(expected_result, result)

	def test_recursive_fibonacci_number_max_recursion_depth_exceeded(self):
		with self.assertRaises(RecursionError):
			find_fibonacci_number_recursive(5000)

	def test_iterative_fibonacci_number(self):
		start_time = time.time()
		result = find_fibonacci_number_iterative(40)
		result_time = time.time() - start_time
		print("\nTiming for finding 40th fibonacci sequence number with iterative method is {} s".format(result_time))
		expected_result = 165580141
		self.assertEqual(expected_result, result)

	def test_golden_ratio_fibonacci_number(self):
		start_time = time.time()
		result = find_fibonacci_number_golden_ratio(40)
		result_time = time.time() - start_time
		print("\nTiming for finding 40th fibonacci sequence number with math golden ratio method is {} s".format(
			result_time))
		expected_result = 165580141
		self.assertEqual(expected_result, result)

	def test_recursive_fibonacci_number_border_values(self):
		self.assertEqual(1, find_fibonacci_number_recursive(0))
		self.assertEqual(1, find_fibonacci_number_recursive(1))
		self.assertEqual(2, find_fibonacci_number_recursive(2))
		self.assertEqual(1, find_fibonacci_number_iterative(0))
		self.assertEqual(1, find_fibonacci_number_iterative(1))
		self.assertEqual(2, find_fibonacci_number_iterative(2))
		self.assertEqual(1, find_fibonacci_number_golden_ratio(0))
		self.assertEqual(1, find_fibonacci_number_golden_ratio(1))
		self.assertEqual(2, find_fibonacci_number_golden_ratio(2))

	def test_negative_inputs(self):
		with self.assertRaises(ValueError):
			find_fibonacci_number_recursive(-1)
			find_fibonacci_number_iterative(-2)
			find_fibonacci_number_golden_ratio(-3)

	def test_wrong_type_inputs(self):
		with self.assertRaises(TypeError):
			find_fibonacci_number_recursive(complex(-1.0, 0.0))
			find_fibonacci_number_iterative("33")
			find_fibonacci_number_golden_ratio("111")

	def test_find_fibonacci_numbers_in_values_range(self):
		with self.assertRaises(ValueError):
			find_fibonacci_numbers_in_values_range(0, 0)
		with self.assertRaises(ValueError):
			find_fibonacci_numbers_in_values_range(1, 1)
		with self.assertRaises(ValueError):
			find_fibonacci_numbers_in_values_range(-5, 1)

		result = find_fibonacci_numbers_in_values_range(0, 100)
		expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		self.assertListEqual(expected_result, result)

		result = find_fibonacci_numbers_in_values_range(1, 34)
		expected_result = [1, 1, 2, 3, 5, 8, 13, 21, 34]
		self.assertListEqual(expected_result, result)

		result = find_fibonacci_numbers_in_values_range(21, 34)
		expected_result = [21, 34]
		self.assertListEqual(expected_result, result)

		result = find_fibonacci_numbers_in_values_range(22, 33)
		expected_result = []
		self.assertListEqual(expected_result, result)
