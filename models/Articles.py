class Articles:
    def __init__(self, name, src="", content="", user=""):
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
