from models.User import User


class Login:
    def __init__(self, user):
        self.__user = user

    def login(self):
        username = self.__user.get_username()
        password = self.__user.get_password()
        user = User()
        result = user.get({"username": username, "password": password})
        return result.__len__() > 0
