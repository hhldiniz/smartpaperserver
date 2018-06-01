import unittest
from models.tests.TestUser import TestUser


class ClientSignup(unittest.TestCase):
    def __init__(self):
        super().__init__()

    def setUp(self):
        test_user = TestUser()
        self.assertEqual(test_user.save(), True, "Signup Test pass!")


class ClientLogin(unittest.TestCase):
    def __init__(self):
        super().__init__()

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
