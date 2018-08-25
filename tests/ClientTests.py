import unittest

from models.tests.TestUser import TestUser


class ClientRegister(unittest.TestCase):

    def setUp(self):
        self.__test_user = TestUser()

    def test_register(self):
        self.assertEqual(self.__test_user.save(), True, "Register Test passed!")

    def tearDown(self):
        self.__test_user.suicide()


class ClientLogin(unittest.TestCase):

    def setUp(self):
        self.__test_user = TestUser()
        self.__test_user.save()

    def test_login(self):
        from utils.DBController import DBController
        db_controller = DBController()
        db_controller.connect()
        result = db_controller.select("users", {"username": self.__test_user.get_username(),
                                                "password": self.__test_user.get_password()})
        self.assertTrue(result is not None, "Login test passed!")

    def tearDown(self):
        self.__test_user.suicide()


if __name__ == '__main__':
    unittest.main()
