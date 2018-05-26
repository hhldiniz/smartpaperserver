from utils.DBController import DBController


class Login:
    def __init__(self, user):
        self.__user = user

    def login(self):
        username = self.__user.get_username()
        password = self.__user.get_password()
        db_controller = DBController(dbname="smartpaper")
        db_controller.connect()
        result = db_controller.select("users", {"username": username, "password": password})
        return result.__len__() > 0
