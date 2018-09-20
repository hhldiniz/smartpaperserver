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
            ranking.append([article, self.__word_count[index]])
        return self.__sort_rank(ranking)

    @staticmethod
    def __sort_rank(ranking):
        i = 0
        j = 0
        while i < len(ranking):
            while j+1 < len(ranking):
                if ranking[i][1] > ranking[j][1]:
                    aux = ranking[i]
                    ranking[i] = ranking[j]
                    ranking[j] = aux
                j += 1
            i += 1
        for obj in ranking:
            print(obj[1])
        return ranking
