# -*- coding: utf-8 -*-

from crawlers.Crawler import Crawler


class ScienceDirectCrawler(Crawler):
    tags = {"article_names": {"class": "result-list-title-link"}, "article_content": None}

    def __init__(self):
        super().__init__("https://www.sciencedirect.com/search?"
                         "qs={{main_key}}"
                         "&authors={{authors}}"
                         "&pub={{publisher}}"
                         "&volume={{volume}}"
                         "&issue={{issue}}"
                         "&page={{page}}"
                         "&origin=home"
                         "&zone=qSearch")
        self.reset_target()

    def set_main_key(self, new_key):
        self.set_target(self.get_target().replace("{{main_key}}", new_key))

    def set_authors(self, new_authors):
        self.set_target(self.get_target().replace("{{authors}}", new_authors))

    def set_publisher(self, new_publisher):
        self.set_target(self.get_target().replace("{{publisher}}", new_publisher))

    def reset_target(self):
        self.set_target(self.get_original_target())
