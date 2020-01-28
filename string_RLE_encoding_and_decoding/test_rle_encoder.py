import unittest
from rle_encoder_decoder import rle_encode_re, rle_decode_re, rle_encode_native, rle_decode_native


class TestRleEncoding(unittest.TestCase):

    def test_rle_encode(self):
        input = "aabddzxxggga"
        result_native = rle_encode_native(input)
        result_re = rle_encode_re(input)
        expected_result = "2a1b2d1z2x3g1a"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = ""
        result_native = rle_encode_native(input)
        result_re = rle_encode_re(input)
        expected_result = ""
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "a"
        result_native = rle_encode_native(input)
        result_re = rle_encode_re(input)
        expected_result = "1a"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "abcdefghijk"
        result_native = rle_encode_native(input)
        result_re = rle_encode_re(input)
        expected_result = "1a1b1c1d1e1f1g1h1i1j1k"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "abbbbbbbbbbbbbbbbbbbbbbbbbbc"
        result_native = rle_encode_native(input)
        result_re = rle_encode_re(input)
        expected_result = "1a26b1c"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

    def test_rle_decode(self):
        input = "2a1b2d1z2x3g1a"
        result_native = rle_decode_native(input)
        result_re = rle_decode_re(input)
        expected_result = "aabddzxxggga"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "1a"
        result_native = rle_decode_native(input)
        result_re = rle_decode_re(input)
        expected_result = "a"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "1a1b1c1d1e1f1g1h1i1j1k"
        result_native = rle_decode_native(input)
        result_re = rle_decode_re(input)
        expected_result = "abcdefghijk"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "1a26b1c"
        result_native = rle_decode_native(input)
        result_re = rle_decode_re(input)
        expected_result = "abbbbbbbbbbbbbbbbbbbbbbbbbbc"
        self.assertEqual(expected_result, result_native)
        self.assertEqual(expected_result, result_re)

        input = "a1b1c1d1e1f1g1h1i1j1k"
        with self.assertRaises(ValueError):
            rle_decode_native(input)
        with self.assertRaises(ValueError):
            rle_decode_re(input)

        input = "1a1b1c1d1e1f1g1h1i1j1"
        with self.assertRaises(ValueError):
            rle_decode_native(input)
        with self.assertRaises(ValueError):
            rle_decode_re(input)

        input = ""
        with self.assertRaises(ValueError):
            rle_decode_native(input)
        with self.assertRaises(ValueError):
            rle_decode_re(input)

        input = "1"
        with self.assertRaises(ValueError):
            rle_decode_native(input)
        with self.assertRaises(ValueError):
            rle_decode_re(input)
