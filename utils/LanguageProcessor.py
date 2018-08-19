class LanguageProcessor:
    def __init__(self, sentence="", language="pt"):
        self.__sentence = sentence
        self.__language = language

    def get_sentence(self):
        return self.__sentence

    def set_sentence(self, sentence):
        self.__sentence = sentence

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

