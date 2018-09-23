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
        for i in range(len(ranking)-1, 0, -1):
            for j in ranking(i):
                if ranking[j][1] > ranking[j + 1][1]:
                    aux = ranking[j]
                    ranking[j] = ranking[j + 1]
                    ranking[j + 1] = aux
        return ranking
