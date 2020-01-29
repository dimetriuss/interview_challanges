import unittest
from scrabble import count_scrabble_scores


class TestScrabble(unittest.TestCase):

    def test_scrabble(self):
        result = count_scrabble_scores("ho")
        expected_result = 5
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores("zihuantanehu")
        expected_result = 27
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores("taxi3")
        expected_result = 11
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores("")
        expected_result = 0
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores("12345678")
        expected_result = 0
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores("ELEPHANT")
        expected_result = 13
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores(5)
        expected_result = 0
        self.assertEqual(expected_result, result)

        result = count_scrabble_scores(5.2325464)
        expected_result = 0
        self.assertEqual(expected_result, result)
