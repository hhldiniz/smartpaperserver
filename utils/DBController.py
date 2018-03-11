from pymongo import MongoClient


class DBController:
    def __init__(self, host="localhost", dbname="test", dbuser="", password="", port=27017):
        self.__host = host
        self.__dbname = dbname
        self.__dbuser = dbuser
        self.__port = port
        self.password = password
        self.__client = None

    def connect(self):
        self.__client = MongoClient(host=self.__host, port=self.__port)

    def get_database(self):
        return self.__client[self.__dbname]

    def get_connection(self):
        return self.__client

    def get_host(self):
        return self.__host

    def get_dbname(self):
        return self.__dbname

    def get_dbuser(self):
        return self.__dbuser

    def set_host(self, new_host):
        self.__host = new_host

    def set_dbname(self, new_dbname):
        self.__dbname = new_dbname
