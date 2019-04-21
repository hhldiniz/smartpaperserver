class RankingPreprocessor:

    def __init__(self, ranking, tags):  # {html_tag: value, article_names: {type: value},
        # article_content: {type: value}, article_link: value|[{type: value}]
        self.__ranking = ranking
        self.__tags = tags
        self.__prepared_ranking = []

    def get_prepared_ranking(self):
        for article in self.__ranking:
            self.__prepared_ranking.append(
                {"name": self.__clean_article_result(article[0].find_all(self.__tags["html_tag"],
                                                                         attrs=self.__tags["article_names"])),
                 "content": ""})
            print(self.__get_article_link(article[0]))
        return self.__prepared_ranking

    @staticmethod
    def __clean_article_result(article_result):
        prepared_article = []
        for article in article_result:
            prepared_article.append(article.get_text())
        return prepared_article

    def __get_article_link(self, article):
        print(self.__tags["article_link"])
        if type(self.__tags["article_link"]) == str:
            return article.find_all(self.__tags["article_link"])
        else:
            return ""
