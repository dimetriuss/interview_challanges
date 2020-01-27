import unittest
from is_sqrt_integer import get_squared_ints_from_range


class TestSqrtIntegers(unittest.TestCase):

    def test_squared_ints_from_range(self):
        result = get_squared_ints_from_range(0, 100)
        expected_result = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertListEqual(expected_result, result)
        result = get_squared_ints_from_range(49, 100)
        expected_result = [49, 64, 81, 100]
        self.assertListEqual(expected_result, result)
        result = get_squared_ints_from_range(50, 63)
        expected_result = []
        self.assertListEqual(expected_result, result)

    def test_get_squared_ints_from_range_validation(self):
        with self.assertRaises(ValueError):
            get_squared_ints_from_range(-1, 1)
        with self.assertRaises(ValueError):
            get_squared_ints_from_range(1, 1)
        with self.assertRaises(TypeError):
            get_squared_ints_from_range(1.28, 10)
        with self.assertRaises(TypeError):
            get_squared_ints_from_range(1, "10")
