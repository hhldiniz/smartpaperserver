import unittest

from utils.Miner import Miner


class NumbersMiningTest(unittest.TestCase):

    def setUp(self):
        self.__miner = Miner(data=[5, 6, 7, 9, 5, 3, 1, 4, 7, 3, 9, 0])

    def test_mine(self):
        self.__miner.mine()


class StringsMiningTest(unittest.TestCase):

    def setUp(self):
        self.__miner = Miner(data=["a", "c", "y", "d", "p", "b", "x", "g"],
                             categories=[
                                 'tecnologia',
                                 'saúde',
                                 'arte',
                                 'música',
                             ])

    def test_mine(self):
        self.__miner.mine()


if __name__ == '__main__':
    unittest.main()
