from views.BaseView import BaseView
from flask import session
from models.Article import Article
from models.User import User


class HistoryView(BaseView):
    def __init__(self, template_name, title="Histórico"):
        super().__init__(template_name, title)

    def get(self, **kwargs):
        articles = Article.get(
            {
                "user.username": session["user"]["username"],
                "user.password": session["user"]["password"]
            })
        user = User.get({"username": session["user"]["username"],
                         "password": session["user"]["password"]})[0]
        kwargs.__setitem__("articles", articles)
        kwargs.__setitem__("user", user)
        return super().get(**kwargs)
