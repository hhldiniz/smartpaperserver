from views.BaseView import BaseView
from flask import session, request
from models.User import User
from miners.ScienceDirectMiner import ScienceDirectMiner


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name, "Index")

    def get(self, **context):
        try:
            user = session["user"]
            context.__setitem__("user", user)
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)

    @staticmethod
    def __search(key):
        miner = ScienceDirectMiner()
        miner.set_main_key(key)
        return miner.send_request()

    def post(self, **context):
        if request.form["hidden"] == "login":
            username = request.form["username"]
            password = request.form["password"]
            user = User(username=username, password=password)
            user = user.get({"username": username, "password": password})
            context.__setattr__("user", user)
        else:
            content = self.__search(request.form["key"])
            content.__setattr__("search_result", content)
        return super().post(**context)
