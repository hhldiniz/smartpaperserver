import os

from utils.DBController import DBController


class Source:
    def __init__(self, url, user):
        self.__url = url
        self.__user = user

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def save(self):
        if os.environ.get("MONGODB_URI") is None:
            db_controller = DBController()
        else:
            db_controller = DBController(uri=os.environ.get("MONGODB_URI"))
            db_controller.set_dbname(os.environ.get("DATABASE"))
        db_controller.connect()
        insert_result = db_controller.insert("sources", {"url": self.get_url(),
                                                         "user": self.get_user()})
        return insert_result.inserted_id is not None

    @staticmethod
    def get(select_filter):
        db_controller = DBController()
        db_controller.connect()
        return db_controller.as_array("sources", select_filter)
