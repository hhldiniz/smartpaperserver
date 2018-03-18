import requests


class HttpClient:
    def __init__(self, target="", timeout=10000, port=80):
        self.__target = target
        self.__timeout = timeout
        self.__port = port

    def get_connection(self, method, params=None):
        if params is None:
            params = {}
        if method == "GET" or method == "get":
            return requests.get(self.get_target(), params=params)
        elif method == "POST" or method == "post":
            return requests.post(self.get_target(), params=params)
        elif method == "PUT" or method == "put":
            return requests.put(self.get_target(), params=params)
        else:
            return requests.delete(self.get_target())

    def set_target(self, new_target):
        self.__target = new_target

    def set_timeout(self, new_timeout):
        self.__timeout = new_timeout

    def set_port(self, new_port):
        self.__port = new_port

    def get_target(self):
        return self.__target
