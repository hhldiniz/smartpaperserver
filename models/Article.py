from utils.DBController import DBController


class Article:
    def __init__(self, name, src="", content="", user=None):
        self.__name = name
        self.__src = src
        self.__content = content
        self.__user = user

    def set_name(self, name):
        self.__name = name

    def set_src(self, src):
        self.__src = src

    def set_content(self, content):
        self.__content = content

    def set_user(self, user):
        self.__user = user

    def get_name(self):
        return self.__name

    def get_src(self):
        return self.__src

    def get_content(self):
        return self.__content

    def get_user(self):
        return self.__user

    def save(self):
        db_controller = DBController()
        db_controller.connect()
        insert_result = db_controller.insert("articles",
                                             {
                                                 "name": self.__name,
                                                 "source": self.__src,
                                                 "content": self.__content,
                                                 "user_id": self.__user.get_id()
                                             })
        return insert_result.inserted_id is not None

    @staticmethod
    def get(select_filter):
        db_controller = DBController()
        db_controller.connect()
        return db_controller.as_array("articles", select_filter)