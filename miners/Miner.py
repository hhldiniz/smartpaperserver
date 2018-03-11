from utils.HttpRequester import HttpClient


class Miner:
    def __init__(self):
        self.__requester = HttpClient()

    def get_requester(self):
        return self.__requester