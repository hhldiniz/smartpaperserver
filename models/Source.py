from utils.DBController import DBController


class Source:
    def __init__(self, url):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def save(self):
        db_controller = DBController()
        db_controller.connect()
        insert_result = db_controller.insert("articles", {"url": self.get_url()})
        return insert_result.inserted_id is not None

    @staticmethod
    def get(select_filter):
        db_controller = DBController()
        db_controller.connect()
        return db_controller.as_array("articles", select_filter)
