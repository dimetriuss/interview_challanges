import unittest
from chars_filter import filter_text


class TestTextCharsFilter(unittest.TestCase):

    def test_vowels_chars_filter(self):
        vowels_filter = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
               'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
               'aliquip ex ea commodo consequat.'
        result_text = filter_text(text, vowels_filter)
        expected_result = "Lrm psm dlr st mt, cnscttr dpscng lt, sd d smd tmpr ncddnt t lbr t dlr mgn lq. t nm d mnm " \
                          "vnm, qs nstrd xrcttn llmc lbrs ns t lqp x  cmmd cnsqt."
        self.assertEqual(result_text, expected_result)

    def test_consonants_chars_filter(self):
        consonants_filter = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                             'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
                             'T', 'V', 'W', 'X', 'Y', 'Z')
        print(type(consonants_filter))
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
               'et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut ' \
               'aliquip ex ea commodo consequat.'
        result_text = filter_text(text, consonants_filter)
        expected_result = "oe iu oo i ae, oeeu aiii ei, e o eiuo eo iiiu u aoe e ooe aa aiua. U ei a ii eia, ui ou" \
                          " eeiaio uao aoi ii u aiui e ea ooo oeua."
        self.assertEqual(result_text, expected_result)

    def test_special_chars_filter(self):
        special_chars_filter = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',')
        text = '($$^Lorem ipsum & dolor #sit @amet, consectetur* adipisc%ing elit!)'
        result_text = filter_text(text, special_chars_filter)
        expected_result = "Lorem ipsum  dolor sit amet consectetur adipiscing elit"
        self.assertEqual(result_text, expected_result)

    def test_spaces_filter(self):
        vowels_filter = (' ', )
        text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ' \
               'et dolore magna aliqua.'
        result_text = filter_text(text, vowels_filter)
        expected_result = "Loremipsumdolorsitamet,consecteturadipiscingelit,seddoeiusmodtemporincididuntutlaboreet" \
                          "doloremagnaaliqua."
        self.assertEqual(result_text, expected_result)
