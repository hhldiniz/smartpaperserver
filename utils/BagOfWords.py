import json
from enum import Enum

from exceptions.WrongBowTypeException import WrongBowTypeException
from utils.BagOfWordsCountMethod import CountMethod
from utils.Ranking import Ranking


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

    def get_bow(self):
        return self.__bow

    def count(self, result_set):
        self.get_words()
        word_count_set = []
        for result in result_set:
            word_sum = 0
            for key in self.__bow.keys():
                if key in str(result):
                    self.__bow[key] += 1
                    word_sum += 1
            word_count_set.append(word_sum)
        print(self.__bow)
        ranking = Ranking(result_set, word_count_set)
        return ranking.prepare_rank()


class BowTypes(Enum):
    FILE = 1
    REMOTE = 2
    NONE = 3
