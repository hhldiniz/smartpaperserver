import unittest

from utils.Miner import Miner


class MiningTest(unittest.TestCase):

    def setUp(self):
        self.__miner = Miner(data=[5, 6, 7, 9, 5, 3, 1, 4, 7, 3, 9, 0])

    def test_mine(self):
        self.__miner.mine()


if __name__ == '__main__':
    unittest.main()
