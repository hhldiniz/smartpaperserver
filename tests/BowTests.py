import unittest

from utils.BagOfWords import BowTypes, Bow


class CompleteBowTest(unittest.TestCase):
    def setUp(self):
        self.bow = Bow(BowTypes.NONE, ["palavra", "palavra2", "palavra3"])

    def test_make_bow(self):
        self.bow.get_words()
        self.assertTrue(self.bow.get_bow() is not None)

    def test_count_word(self):
        self.bow.get_words()
        self.bow.count_words("palavra2 palavra3")


if __name__ == '__main__':
    unittest.main()
