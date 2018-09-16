import json
from datetime import datetime

from flask import session, request

from crawlers.ACMCrawler import ACMCrawler
from crawlers.ScienceDirectCrawler import ScienceDirectCrawler
from models.Article import Article
from models.User import User
from utils.BagOfWords import Bow, BowTypes
from utils.Miner import Miner
from views.BaseView import BaseView


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name, "Index")

    @staticmethod
    def __get_user_obj():
        try:
            username = session["user"]["username"]
            password = session["user"]["password"]
            user = User(username=username, password=password)
            user = user.get({"username": username, "password": password})[0]
            return user
        except KeyError:
            return None

    def get(self, **context):
        try:
            user = session["user"]
            context.__setitem__("user", user)
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)

    @staticmethod
    def __search(key, user):
        science_direct_crawler = ScienceDirectCrawler()
        acm_crawler = ACMCrawler()
        acm_crawler.set_main_key(key)
        # acm_crawler.search({"class": "details"})
        science_direct_crawler.set_main_key(key)
        content = science_direct_crawler.search({"class": "result-item-content"})
        bow = Bow(BowTypes.FILE, "utils/dictionary.json")
        bow.count(content)
        miner = Miner(data=content)
        # miner.mine()
        if user is not None:
            article = Article(datetime.now().timestamp(), science_direct_crawler.get_original_target(), content, user)
            article.save()
        return content

    def post(self, **context):
        try:
            if request.form["hidden"] == "login":
                context.__setattr__("user", self.__get_user_obj())
                return super().post(**context)
            else:
                content = self.__search(request.form["key"], self.__get_user_obj())
                return json.dumps({"search_result": str(content)})
        except KeyError:
            content = self.__search(request.form["key"], self.__get_user_obj())
            return json.dumps({"search_result": str(content)})
