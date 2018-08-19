import json
from datetime import datetime

from flask import session, request

from miners.ScienceDirectMiner import ScienceDirectMiner
from models.Article import Article
from models.User import User
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
        miner = ScienceDirectMiner()
        miner.set_main_key(key)
        content = miner.search({"class": "result-item-content"})
        print(content)
        # language_processor = LanguageProcessor(content)
        if user is not None:
            article = Article(datetime.now().timestamp(), miner.get_original_target(), content, user)
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
