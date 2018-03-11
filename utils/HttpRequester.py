from http import client


class HttpClient:
    def __init__(self, target="", timeout=10000, port=80):
        self.__target = target
        self.__timeout = timeout
        self.__port = port

    def get_connection(self):
        return client.HTTPConnection(host=self.__target, port=self.__port, timeout=self.__timeout)

    def set_target(self, new_target):
        self.__target = new_target

    def set_timeout(self, new_timeout):
        self.__timeout = new_timeout

    def set_port(self, new_port):
        self.__port = new_port

    def get_target(self):
        return self.__target
