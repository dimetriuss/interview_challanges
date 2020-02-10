import unittest
from staircase import staircase


class TestStaircase(unittest.TestCase):

    def test_staircase(self):
        result = staircase(10)
        expected_result = ['         #', '        ##', '       ###', '      ####', '     #####', '    ######',
                           '   #######', '  ########', ' #########', '##########']
        self.assertEqual(expected_result, result)
        print()
        for line in result:
            print(line)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            staircase(0)
        with self.assertRaises(ValueError):
            staircase(101)
