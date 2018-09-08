import urllib.request as request
from enum import Enum

from exceptions.WrongBowTypeException import WrongBowTypeException


class Bow:
    def __init__(self, source_type, source):
        self.__source_type = source_type
        self.__source = source
        self.__bow = None

    def get_words(self):
        bow = {}
        if self.__source_type == BowTypes.FILE:
            file = open(self.__source, "r")
            for word in file.readline():
                bow.__setitem__(word, 0)
        elif self.__source_type == BowTypes.REMOTE:
            for word in list(request.urlopen(self.__source).read()):
                bow.__setitem__(word, 0)
        elif self.__source_type == BowTypes.NONE:
            for word in self.__source:
                bow.__setitem__(word, 0)
        else:
            raise WrongBowTypeException("Bow type is not known")
        self.__bow = bow

    def get_bow(self):
        return self.__bow

    def count_words(self, text):
        text = text.split()
        for word in text:
            try:
                self.get_bow()[word] += 1
            except KeyError:
                pass


class BowTypes(Enum):
    FILE = 1
    REMOTE = 2
    NONE = 3
