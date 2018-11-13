from pymongo import MongoClient


class DBController:
    def __init__(self, host="localhost", dbname="test", dbuser="", password="", port=27017, uri=None):
        self.__host = host
        self.__dbname = dbname
        self.__dbuser = dbuser
        self.__port = port
        self.__password = password
        self.__uri = uri
        self.__client = None

    def connect(self):
        if self.__uri is None:
            self.__client = MongoClient(host=self.__host, port=self.__port)
        else:
            self.__client = MongoClient(self.__uri)

    def select(self, collection, params=None):
        if params is None:
            params = {}
        db = self.get_database()
        collection = db[collection]
        if params.__len__() == 0:
            return collection.find()
        elif params.__len__() == 1:
            return collection.find_one(params, projection={"_id": False})
        else:
            return collection.find(params, projection={"_id": False})

    def as_array(self, collection, params=None):
        result = []
        for document in self.select(collection, params):
            result.append(document)
        return result

    def insert(self, collection, document):
        db = self.get_database()
        collection = db[collection]
        return collection.insert_one(document)

    def delete(self, collection, params):
        db = self.get_database()
        collection = db[collection]
        return collection.delete_one(params)

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
