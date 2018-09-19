class Ranking:
    def __init__(self, article_set, word_count_set):
        self.__article_set = article_set
        self.__word_count = word_count_set

    def get_word_count(self):
        return self.__word_count

    def get_article_set(self):
        return self.__article_set

    def prepare_rank(self):
        ranking = []
        for index, article in enumerate(self.__article_set):
            ranking.append((article, self.__word_count[index]))
        return self.__sort_rank(ranking)

    @staticmethod
    def __sort_rank(ranking):
        for index, obj in enumerate(ranking):
            for index2, obj2 in enumerate(obj):
                if obj[1] < obj2[1]:
                    aux = obj
                    ranking[index] = ranking[index2]
                    ranking[index2] = aux
        print(ranking)
        return ranking
