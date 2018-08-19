import ssl
import urllib.request as request

from bs4 import BeautifulSoup


class Miner:
    def __init__(self, original_url):
        self.__original_target = original_url
        self.__target = self.__original_target

    def get_original_target(self):
        return self.__original_target

    def get_target(self):
        return self.__target

    def set_target(self, target):
        self.__target = target

    def send_request(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        return request.urlopen(self.get_target(), context=context).read()

    def parse(self):
        return BeautifulSoup(self.send_request(), 'html5lib')

    def search(self, args):
        return self.parse().find_all(args)
