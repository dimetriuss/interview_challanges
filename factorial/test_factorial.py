import unittest
import time
from factorial import calculate_factorial_iterative, calculate_factorial_recursive, calculate_factorial_core_lib_method


class TestFactorialCalculation(unittest.TestCase):

	def test_iterative_factorial_calculation(self):
		results = []
		start_time = time.time()
		for i in range(0, 10):
			results.append(calculate_factorial_iterative(i))
		result_time = time.time() - start_time
		print("\nTiming for iterative factorial calculations for numbers in range(0, 10) is {} s".format(result_time))
		expected_results = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
		self.assertListEqual(expected_results, results)

	def test_recursive_factorial_calculation(self):
		results = []
		start_time = time.time()
		for i in range(0, 10):
			results.append(calculate_factorial_recursive(i))
		result_time = time.time() - start_time
		print("\nTiming for recursive factorial calculations for numbers in range(0, 10) is {} s".format(result_time))
		expected_results = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
		self.assertListEqual(expected_results, results)

	def test_math_module_factorial_calculation(self):
		results = []
		start_time = time.time()
		for i in range(0, 10):
			results.append(calculate_factorial_core_lib_method(i))
		result_time = time.time() - start_time
		print("\nTiming for core factorial calculations for numbers in range(0, 10) is {} s".format(result_time))
		expected_results = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
		self.assertListEqual(expected_results, results)

	def test_negative_inputs(self):
		with self.assertRaises(ValueError):
			calculate_factorial_iterative(-1)
			calculate_factorial_recursive(-5)
			calculate_factorial_core_lib_method(-10)

	def test_wrong_type_inputs(self):
		with self.assertRaises(TypeError):
			calculate_factorial_iterative(3.14)
			calculate_factorial_recursive(complex(-1.0, 0.0))
			calculate_factorial_core_lib_method("33")
