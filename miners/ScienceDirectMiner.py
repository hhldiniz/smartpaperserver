from miners.Miner import Miner
import re


class ScienceDirectMiner(Miner):
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

    def set_main_key(self, new_key):
        requester = self.get_requester()
        requester.set_target(requester.get_target().replace("{{main_key}}", new_key))

    def set_authors(self, new_authors):
        requester = self.get_requester()
        requester.set_target(requester.get_target().replace("{{authors}}", new_authors))

    def set_publisher(self, new_publisher):
        requester = self.get_requester()
        requester.set_target(requester.get_target().replace("{{publisher}}", new_publisher))

    def reset_target(self):
        self.get_requester().set_target(self.get_original_target())

    def send_request(self):
        requester = self.get_requester()
        regex = re.compile(r"{{\w+\}\}")
        regex.sub(requester.set_target(requester.get_target()), "")
