import re
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
        self._clean_url()
        print(self.get_target())
        if type(args) == dict:
            return self.parse().find_all(attrs=args)
        return self.parse().find_all(args)

    def search_by_tag_and_class(self, tag, value):
        return self.parse().find_all(tag, class_=value)

    def _clean_url(self):
        m = re.compile("({{\w+}})")
        result = m.findall(self.get_target())
        for obj in result:
            self.set_target(self.get_target().replace(obj, ""))
