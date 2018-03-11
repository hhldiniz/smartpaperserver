from utils.HttpRequester import HttpClient


class Miner:
    def __init__(self, original_url):
        self.__requester = HttpClient()
        self.__original_target = original_url

    def get_requester(self):
        return self.__requester

    def get_original_target(self):
        return self.__original_target
