import unittest
from time_converter_12_to_24_hours import convert_time_12_to_24_hours


class TestTimeConverter(unittest.TestCase):

    def test_12_to_24_time_converter(self):
        time = "12:00:00AM"
        result_time = convert_time_12_to_24_hours(time)
        expected_time = "00:00:00"
        self.assertEqual(result_time, expected_time)
        
        time = "08:59:59AM"
        result_time = convert_time_12_to_24_hours(time)
        expected_time = "08:59:59"
        self.assertEqual(result_time, expected_time)

        time = "12:00:00PM"
        result_time = convert_time_12_to_24_hours(time)
        expected_time = "12:00:00"
        self.assertEqual(result_time, expected_time)

        time = "01:05:45PM"
        result_time = convert_time_12_to_24_hours(time)
        expected_time = "13:05:45"
        self.assertEqual(result_time, expected_time)

        time = "07:05:45PM"
        result_time = convert_time_12_to_24_hours(time)
        expected_time = "19:05:45"
        self.assertEqual(result_time, expected_time)
