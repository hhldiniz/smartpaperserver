import json
from enum import Enum

from exceptions.WrongBowTypeException import WrongBowTypeException
from utils.BagOfWordsCountMethod import CountMethod


class Bow(CountMethod):
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
            json_file = open("dictionary.json")
            print(json_file.read())
            bow = json.load(json_file)
        elif self.__source_type == BowTypes.NONE:
            for word in self.__source:
                bow.__setitem__(word, 0)
        else:
            raise WrongBowTypeException("Bow type is not known")
        self.__bow = bow
        print(bow)

    def get_bow(self):
        return self.__bow

    def count(self, result_set):
        self.get_words()
        for key in self.__bow.keys():
            for word in result_set:
                if word == key:
                    self.__bow[key] += 1


class BowTypes(Enum):
    FILE = 1
    REMOTE = 2
    NONE = 3
