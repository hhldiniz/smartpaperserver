from crawlers.Crawler import Crawler


class ScieloCrawler(Crawler):

    tags = {"html_tag": "strong", "article_names": {"class": "title"}, "article_content": None}

    def __init__(self):
        super().__init__("https://search.scielo.org/?q={{main_key}}&where=ORG")

    def set_main_key(self, new_key):
        self.set_target(self.get_target().replace("{{main_key}}", new_key))

    def reset_target(self):
        self.set_target(self.get_original_target())
