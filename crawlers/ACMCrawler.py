from crawlers.Crawler import Crawler


class ACMCrawler(Crawler):
    def __init__(self):
        super().__init__("https://dl.acm.org/results.cfm?query={{main_key}}")
        self.reset_target()

    def reset_target(self):
        self.set_target(self.get_original_target())

    def set_main_key(self, new_key):
        self.set_main_key((self.get_target().replace("{{main_key}}", new_key)))
